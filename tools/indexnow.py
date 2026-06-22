#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스.

IndexNow 프로토콜은 한 엔드포인트에 제출하면 참여 검색엔진끼리 공유하지만,
네이버·빙에 확실히 닿도록 주요 엔드포인트에 모두 통보한다.

사용법:
  python tools/indexnow.py                # sitemap.xml 의 모든 URL 통보 (첫 일괄 통보)
  python tools/indexnow.py URL [URL ...]  # 지정한 URL 만 통보 (글 올릴 때마다)

전제:
  - 배포 후 루트에 "{INDEXNOW_KEY}.txt" 파일이 접근 가능해야 한다 (build.py 가 생성).
  - 의존성 없음(파이썬 표준 라이브러리만 사용).
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# 통보 대상 엔드포인트 (중복 제출은 무해함)
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(endpoint: str, urls: list) -> None:
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  [{resp.status}] {endpoint}")
    except urllib.error.HTTPError as e:
        # 200/202 외 코드도 본문에 사유가 있을 수 있어 함께 출력
        body = e.read().decode("utf-8", "replace")[:200]
        print(f"  [{e.code}] {endpoint}  {body}")
    except Exception as e:  # noqa: BLE001
        print(f"  [ERR] {endpoint}  {e}")


def main() -> None:
    urls = sys.argv[1:] if len(sys.argv) > 1 else urls_from_sitemap()
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    # IndexNow 는 요청당 최대 10,000 URL
    print(f"IndexNow 통보: {len(urls)} URL → host={HOST}")
    for u in urls:
        print("  ·", u)
    for ep in ENDPOINTS:
        submit(ep, urls)
    print("완료. (202/200 = 접수 성공)")


if __name__ == "__main__":
    main()
