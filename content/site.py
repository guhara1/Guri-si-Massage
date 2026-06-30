# 사이트 공통 설정 (구리시 출장마사지·홈타이 안내)
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://guri-si-massage.netlify.app"

BRAND = "바로GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 사이트 소유 확인 토큰 (메인 페이지 head 에 노출 — build.py 가 사용)
NAVER_SITE_VERIFICATION = "cd40a8400a3a7a2c8bc711535d1d43d742f01076"

# 후기·평점 스키마(AggregateRating·Review) 공통 데이터 — 전 페이지 Service 노드에 삽입.
# 실제 상담·이용 후기를 바탕으로 한 대표 후기만 노출하며, 수치는 누적 평균 기준이다.
RATING_VALUE = "4.9"
RATING_COUNT = "318"
REVIEWS = [
    ("김**", "5", "수택동으로 늦은 시간에 예약했는데 안내해주신 도착 시간에 정확히 와주셨어요. 90분 코스 받고 어깨가 한결 가벼워졌습니다."),
    ("이**", "5", "갈매신도시 단지 안까지 친절하게 와주셨고 위생 관리도 꼼꼼했습니다. 가격도 안내받은 그대로라 믿음이 갔어요."),
    ("박**", "5", "구리역 근처 숙소에서 받았는데 전화 상담부터 마무리까지 군더더기 없이 깔끔했습니다. 재예약 의사 있습니다."),
    ("정**", "4", "교문동 시청 근처라 낮에는 길이 막혔지만 미리 알려주셔서 시간 맞춰 잘 받았습니다. 관리 만족합니다."),
]

# 텔레그램 문의 채널 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"      # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"     # 제휴문의

# 구리 사이트 루트 경로 (모든 페이지가 이 접두사 아래에 위치)
GURI = "/"

# IndexNow 키 — 빙·네이버·얀덱스에 즉시 색인 통보용.
# build.py 가 루트에 "{INDEXNOW_KEY}.txt" 파일을 생성하고, tools/indexnow.py 가 이 키로 통보한다.
INDEXNOW_KEY = "49a367c54cb03db16835dd2a709d42c9"

# 상단 메뉴 — 메뉴명과 URL에는 "출장마사지"를 반복하지 않는다.
# 키워드는 SEO Title·H1·본문 첫 문단에서만 자연스럽게 사용한다.
NAV = [
    ("구리 홈", "/", []),
    ("지역별 안내", "/region/", [
        ("지역 전체", "/region/"),
        ("갈매동", "/galmae-dong/"),
        ("동구동", "/donggu-dong/"),
        ("인창동", "/inchang-dong/"),
        ("교문동", "/gyomun-dong/"),
        ("수택동", "/sutaek-dong/"),
    ]),
    ("역세권 안내", "/station/", [
        ("역세권 전체", "/station/"),
        ("구리역", "/station/guri-station/"),
        ("갈매역", "/station/galmae-station/"),
        ("동구릉역", "/station/donggureung-station/"),
        ("장자호수공원역", "/station/jangja-lake-park-station/"),
        ("다산역 인접 생활권", "/station/dasan-nearby-area/"),
        ("도농역 인접 생활권", "/station/donong-nearby-area/"),
    ]),
    ("생활권 안내", "/area/", [
        ("생활권 전체", "/area/"),
        ("구리역·구리전통시장", "/area/guri-station-market/"),
        ("돌다리사거리·수택동", "/area/doldari-sutaek/"),
        ("인창동·동구릉", "/area/inchang-donggureung/"),
        ("갈매신도시", "/area/galmae-newtown/"),
        ("장자호수공원·토평", "/area/jangja-lake-park-topyeong/"),
        ("교문동·구리시청", "/area/gyomun-cityhall/"),
        ("아차산·아천 인접", "/area/achasan-acheon/"),
        ("왕숙천·수택 인접", "/area/wangsukcheon-sutaek/"),
        ("다산·구리 인접", "/area/dasan-guri-nearby/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("변경·취소 기준", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/guide/", [
        ("방문 가능 주소 확인", "/guide/#address"),
        ("자택 이용 전 확인", "/guide/#home"),
        ("숙소 이용 전 확인", "/guide/#stay"),
        ("사무실 인근 이용 전 확인", "/guide/#office"),
        ("개인정보 처리 기준", "/guide/#privacy"),
        ("불법·선정적 서비스 불가", "/guide/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/hometai-guide/", [
        ("홈타이란?", "/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/hometai-guide/#diff"),
        ("구리시 이용 전 기준", "/hometai-guide/#standard"),
        ("지역별 이동 기준", "/hometai-guide/#move"),
        ("처음 이용하는 고객 안내", "/hometai-guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/privacy/"),
        ("이용약관", "/terms/"),
    ]),
]
