# 사이트 공통 설정 (구리시 출장마사지·홈타이 안내)
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.barogo-guri.example.com"

BRAND = "바로GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 텔레그램 문의 채널 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"      # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"     # 제휴문의

# 구리 사이트 루트 경로 (모든 페이지가 이 접두사 아래에 위치)
GURI = "/gyeonggi/guri/"

# 상단 메뉴 — 메뉴명과 URL에는 "출장마사지"를 반복하지 않는다.
# 키워드는 SEO Title·H1·본문 첫 문단에서만 자연스럽게 사용한다.
NAV = [
    ("구리 홈", "/gyeonggi/guri/", []),
    ("지역별 안내", "/gyeonggi/guri/region/", [
        ("지역 전체", "/gyeonggi/guri/region/"),
        ("갈매동", "/gyeonggi/guri/galmae-dong/"),
        ("동구동", "/gyeonggi/guri/donggu-dong/"),
        ("인창동", "/gyeonggi/guri/inchang-dong/"),
        ("교문동", "/gyeonggi/guri/gyomun-dong/"),
        ("수택동", "/gyeonggi/guri/sutaek-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/guri/station/", [
        ("역세권 전체", "/gyeonggi/guri/station/"),
        ("구리역", "/gyeonggi/guri/station/guri-station/"),
        ("갈매역", "/gyeonggi/guri/station/galmae-station/"),
        ("동구릉역", "/gyeonggi/guri/station/donggureung-station/"),
        ("장자호수공원역", "/gyeonggi/guri/station/jangja-lake-park-station/"),
        ("다산역 인접 생활권", "/gyeonggi/guri/station/dasan-nearby-area/"),
        ("도농역 인접 생활권", "/gyeonggi/guri/station/donong-nearby-area/"),
    ]),
    ("생활권 안내", "/gyeonggi/guri/area/", [
        ("생활권 전체", "/gyeonggi/guri/area/"),
        ("구리역·구리전통시장", "/gyeonggi/guri/area/guri-station-market/"),
        ("돌다리사거리·수택동", "/gyeonggi/guri/area/doldari-sutaek/"),
        ("인창동·동구릉", "/gyeonggi/guri/area/inchang-donggureung/"),
        ("갈매신도시", "/gyeonggi/guri/area/galmae-newtown/"),
        ("장자호수공원·토평", "/gyeonggi/guri/area/jangja-lake-park-topyeong/"),
        ("교문동·구리시청", "/gyeonggi/guri/area/gyomun-cityhall/"),
        ("아차산·아천 인접", "/gyeonggi/guri/area/achasan-acheon/"),
        ("왕숙천·수택 인접", "/gyeonggi/guri/area/wangsukcheon-sutaek/"),
        ("다산·구리 인접", "/gyeonggi/guri/area/dasan-guri-nearby/"),
    ]),
    ("예약 안내", "/gyeonggi/guri/reservation/", [
        ("예약 방법", "/gyeonggi/guri/reservation/#how"),
        ("예약 가능 시간", "/gyeonggi/guri/reservation/#hours"),
        ("방문 가능 장소", "/gyeonggi/guri/reservation/#place"),
        ("추가 이동비 안내", "/gyeonggi/guri/reservation/#move"),
        ("결제 방식 안내", "/gyeonggi/guri/reservation/#payment"),
        ("변경·취소 기준", "/gyeonggi/guri/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/gyeonggi/guri/guide/", [
        ("방문 가능 주소 확인", "/gyeonggi/guri/guide/#address"),
        ("자택 이용 전 확인", "/gyeonggi/guri/guide/#home"),
        ("숙소 이용 전 확인", "/gyeonggi/guri/guide/#stay"),
        ("사무실 인근 이용 전 확인", "/gyeonggi/guri/guide/#office"),
        ("개인정보 처리 기준", "/gyeonggi/guri/guide/#privacy"),
        ("불법·선정적 서비스 불가", "/gyeonggi/guri/guide/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/gyeonggi/guri/hometai-guide/", [
        ("홈타이란?", "/gyeonggi/guri/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/gyeonggi/guri/hometai-guide/#diff"),
        ("구리시 이용 전 기준", "/gyeonggi/guri/hometai-guide/#standard"),
        ("지역별 이동 기준", "/gyeonggi/guri/hometai-guide/#move"),
        ("처음 이용하는 고객 안내", "/gyeonggi/guri/hometai-guide/#first"),
    ]),
    ("고객센터", "/gyeonggi/guri/support/", [
        ("공지사항", "/gyeonggi/guri/support/#notice"),
        ("자주 묻는 질문", "/gyeonggi/guri/support/#faq"),
        ("1:1 문의", "/gyeonggi/guri/support/#contact"),
        ("제휴·기업 문의", "/gyeonggi/guri/support/#biz"),
        ("사이트 소개", "/gyeonggi/guri/about/"),
        ("개인정보 처리방침", "/gyeonggi/guri/privacy/"),
        ("이용약관", "/gyeonggi/guri/terms/"),
    ]),
]
