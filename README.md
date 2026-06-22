# 바로GO — 구리시 출장마사지·홈타이 지역 안내 사이트

경기도 구리시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·구조화 데이터·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조·텔레그램 링크
  pricing.py        # 코스별 기본 요금 공용 블록
  main.py           # 메인 페이지 (+ FAQPage JSON-LD)
  areas.py          # 지역별: 구리 허브 + 대표 동 5개 (갈매·동구·인창·교문·수택)
  stations.py       # 역세권별: 허브 + 6개 (구리·갈매·동구릉·장자호수공원 + 다산·도농 인접)
  localareas.py     # 생활권별: 허브 + 9개 거점 생활권
  info.py           # 예약·이용 전 확인·홈타이 가이드·고객센터·개인정보·약관
  about.py          # 사이트 소개 (E-E-A-T: Who/How/Why)
assets/             # CSS(프리미엄 팔레트·오버레이), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 색인 여부 리포트가 출력됩니다. 메인 페이지는 루트 `/`에 바로 생성됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외 (개인정보·약관·고객센터 등 유틸리티 페이지)
- 모든 색인 페이지에 **Organization · WebPage · BreadcrumbList · ImageObject** 구조화 데이터 자동 삽입
- 오프라인 사업장 주소가 없는 방문형 사이트이므로 **LocalBusiness Schema 미사용**
- 대표동은 5개만 (갈매·동구·인창·교문·수택) — 번호 행정동(교문1/2, 수택1/2/3) 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(구리역)도 URL 하나, 노선별 페이지 없음
- 메뉴·URL에 "출장마사지" 미반복 — 키워드는 Title·H1·메타·첫 문단에서만 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 모든 페이지 메타 디스크립션 80자 이내

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt·구조화 데이터에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
