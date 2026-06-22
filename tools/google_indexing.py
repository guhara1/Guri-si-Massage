#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 (선택).

구글은 IndexNow 에 참여하지 않으므로, 즉시 통보가 필요하면 이 스크립트를 쓴다.
(구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 대상이지만, 일반 URL 에도
통보가 접수되는 경우가 많다. 보장은 없으며 정식 경로는 Search Console 색인 요청·사이트맵이다.)

사전 설정(한 번만):
  1) Google Cloud 프로젝트 생성 → "Indexing API" 사용 설정.
  2) 서비스 계정 생성 → JSON 키 파일 다운로드.
  3) Search Console > 설정 > 사용자 및 권한 에서 그 서비스 계정 이메일을
     "소유자(Owner)" 로 추가.
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
  python tools/google_indexing.py                # sitemap.xml 전체 통보
  python tools/google_indexing.py URL [URL ...]  # 지정 URL 통보
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def main() -> None:
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred or not os.path.exists(cred):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 없습니다: pip install google-auth requests")

    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    session = AuthorizedSession(creds)

    urls = sys.argv[1:] if len(sys.argv) > 1 else urls_from_sitemap()
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    print(f"구글 Indexing API 통보: {len(urls)} URL")
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        print(f"  [{status}] {u}")
        if r.status_code != 200:
            print("    ", r.text[:200])
    print("완료.")


if __name__ == "__main__":
    main()
