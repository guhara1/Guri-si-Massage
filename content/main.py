# 메인 페이지 — 구리시 출장마사지·홈타이 허브.
# 모든 키워드를 밀어 넣지 않고 대표동·역세권·생활권 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY, GURI
from .pricing import PRICING

_GURI_URL = BASE_URL.rstrip("/") + GURI

# 사이트 소유 확인 메타 태그(naver-site-verification)는 build.py 가
# content.site.NAVER_SITE_VERIFICATION 값을 메인 페이지 head 에 자동 삽입한다.

# 오프라인 사업장 주소가 없는 방문형 사이트이므로 LocalBusiness 계열은 쓰지 않는다.
# Organization·WebPage·BreadcrumbList 는 build.py 가 전 페이지에 자동 삽입하고,
# 메인 페이지에는 FAQPage 만 추가한다.
_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "구리시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 갈매동, 동구동, 인창동, 교문동, 수택동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "구리역이나 장자호수공원역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "구리역, 갈매역, 동구릉역, 장자호수공원역 등 주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "교문1동·수택2동처럼 번호가 붙은 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "교문1·2동은 교문동, 수택1·2·3동은 수택동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "다산역·도농역 쪽도 안내가 되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "다산역과 도농역은 남양주시 성격이 강해 구리 사이트에서는 인접 생활권 이동 기준으로만 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이는 집에서 받는 타이마사지를 가리키는 말로 출장마사지의 대표 형태입니다. 자세한 차이는 홈타이 이용 가이드에서 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 경기도 구리시 전지역</p>
    <h1>구리시 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·숙소·사무실 인근 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>5개</strong><span>대표 동</span></li>
      <li><strong>6개</strong><span>역세권 안내</span></li>
      <li><strong>9개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>구리시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>구리시 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 구리시는 면적이 크지는 않지만 갈매동, 인창동, 교문동, 수택동, 동구동의 생활권 차이가 뚜렷합니다. 구리역과 구리전통시장 주변은 중심 상권 성격이 강하고, 수택동과 장자호수공원 주변은 주거지와 상권이 함께 연결됩니다. 갈매동은 신도시형 주거 생활권이고, 동구동과 인창동은 동구릉역과 인창동 주거지, 사노동 인접권을 함께 설명해야 합니다. 그래서 이 사이트는 "구리 전지역 가능"만 반복하는 방식 대신, 대표동과 역세권, 생활권을 나누어 안내하는 구조로 만들었습니다. 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 함께 확인하시는 것이 좋습니다. 자세한 절차는 <a href="/reservation/">구리시 방문 예약 안내</a>에서 단계별로 정리했습니다.</p>
</section>

<section id="difference">
<h2>갈매동·인창동·교문동·수택동 생활권 차이</h2>
<p>같은 구리시라도 동마다 주거 형태와 생활 리듬이 다릅니다. 갈매동은 구리 북쪽의 <a href="/area/galmae-newtown/">갈매신도시 생활권</a>으로 아파트 단지와 갈매역 접근성이 중심이고, 인창동은 구리역과 동구릉역 사이의 주거 생활권입니다. 교문동은 구리시청과 교문사거리, 아차산 인접권을 아우르고, 수택동은 구리역·돌다리사거리·장자호수공원역·토평 인접권이 함께 연결되는 구리시에서 가장 넓은 생활권입니다. 동구동은 동구릉역과 사노동, 동구릉 인접권을 함께 안내합니다. 동네별 분위기가 다른 만큼 방문 시간대나 차량 이동 기준에 대한 안내도 조금씩 달라집니다. 거주하시거나 머무시는 동의 특징은 <a href="/region/">구리시 지역별 안내</a>에서 한눈에 비교할 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표동은 갈매동, 동구동, 인창동, 교문동, 수택동으로 구성합니다. 번호로 나뉜 교문1·2동과 수택1·2·3동은 각각 교문동·수택동 대표 페이지로 통합하고, 사노동·토평동·아천동은 단독 페이지 대신 인접 동과 생활권 페이지에서 보조 설명합니다. 같은 본문에서 지역명만 바꾸는 방식을 피하고, 각 페이지는 고유한 생활권 정보로 채웠습니다.</p>
<ul class="card-grid">
<li><a href="/galmae-dong/">갈매동</a></li>
<li><a href="/donggu-dong/">동구동</a></li>
<li><a href="/inchang-dong/">인창동</a></li>
<li><a href="/gyomun-dong/">교문동</a></li>
<li><a href="/sutaek-dong/">수택동</a></li>
</ul>
<p>수택동은 구리시 안에서도 검색 의도가 가장 넓은 대표 생활권이라, <a href="/sutaek-dong/">수택동 방문 관리 안내</a>에서 돌다리사거리, 구리전통시장, 장자호수공원역, 토평동 인접권을 함께 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>구리역·갈매역·동구릉역·장자호수공원역 역세권 안내</h2>
<p>구리시는 수도권 전철 8호선(별내선)과 경의중앙선, 경춘선이 지나면서 역 기준으로 위치를 설명하는 분이 많습니다. 역세권 페이지는 역마다 한 페이지씩만 운영하며, 구리역은 경의중앙선과 8호선이 만나도 노선별로 쪼개지 않고 하나의 페이지로 안내합니다. 다산역과 도농역은 남양주시 성격이 강해 인접 생활권 이동 기준으로만 다룹니다.</p>
<ul class="card-grid">
<li><a href="/station/guri-station/">구리역</a></li>
<li><a href="/station/galmae-station/">갈매역</a></li>
<li><a href="/station/donggureung-station/">동구릉역</a></li>
<li><a href="/station/jangja-lake-park-station/">장자호수공원역</a></li>
<li><a href="/station/dasan-nearby-area/">다산역 인접</a></li>
<li><a href="/station/donong-nearby-area/">도농역 인접</a></li>
</ul>
<p>역과 생활권을 함께 확인하고 싶다면 <a href="/area/">구리시 생활권 안내</a>에서 구리역·구리전통시장, 돌다리사거리·수택동, 장자호수공원·토평 같은 거점 기준 안내를 참고해 주세요.</p>
</section>

<section id="topics">
<h2>구리시 동네별·거점별 출장마사지·홈타이 주제 모아보기</h2>
<p>찾으시는 위치를 더 빠르게 연결해 드리기 위해, 구리시에서 많이 찾는 동네·역세권·생활권 주제를 한곳에 모았습니다. 익숙한 지명을 골라 누르시면 해당 지역의 방문 가능 범위와 이동 기준, 예약 전 확인사항으로 바로 이동합니다.</p>

<div class="topic-hub">
  <p class="topic-group-title">대표 동별 방문 관리</p>
  <ul class="topic-grid">
    <li><a href="/galmae-dong/"><span class="topic-name">갈매동 출장마사지·홈타이</span><span class="topic-desc">갈매역·갈매신도시·별내 인접 생활권</span></a></li>
    <li><a href="/donggu-dong/"><span class="topic-name">동구동 출장마사지·홈타이</span><span class="topic-desc">동구릉역·사노동·동구릉 인접권</span></a></li>
    <li><a href="/inchang-dong/"><span class="topic-name">인창동 출장마사지·홈타이</span><span class="topic-desc">구리역·동구릉역 사이 중심부 주거지</span></a></li>
    <li><a href="/gyomun-dong/"><span class="topic-name">교문동 출장마사지·홈타이</span><span class="topic-desc">구리시청·교문사거리 행정 중심</span></a></li>
    <li><a href="/sutaek-dong/"><span class="topic-name">수택동 출장마사지·홈타이</span><span class="topic-desc">구리역·돌다리사거리·장자호수공원</span></a></li>
  </ul>

  <p class="topic-group-title">역세권별 이동 기준</p>
  <ul class="topic-grid">
    <li><a href="/station/guri-station/"><span class="topic-name">구리역 출장마사지 안내</span><span class="topic-desc">경의중앙선·8호선 환승 중심 상권</span></a></li>
    <li><a href="/station/galmae-station/"><span class="topic-name">갈매역 출장마사지 안내</span><span class="topic-desc">경춘선 갈매역·신도시 단지권</span></a></li>
    <li><a href="/station/donggureung-station/"><span class="topic-name">동구릉역 출장마사지 안내</span><span class="topic-desc">8호선 별내선·인창·동구동 연결</span></a></li>
    <li><a href="/station/jangja-lake-park-station/"><span class="topic-name">장자호수공원역 출장마사지 안내</span><span class="topic-desc">별내선·수택·토평 주거 단지</span></a></li>
    <li><a href="/station/dasan-nearby-area/"><span class="topic-name">다산역 인접 이동 안내</span><span class="topic-desc">수택동·왕숙천 방면 인접 생활권</span></a></li>
    <li><a href="/station/donong-nearby-area/"><span class="topic-name">도농역 인접 이동 안내</span><span class="topic-desc">인창동·구리 중심권 인접 생활권</span></a></li>
  </ul>

  <p class="topic-group-title">생활권 거점별 안내</p>
  <ul class="topic-grid">
    <li><a href="/area/guri-station-market/"><span class="topic-name">구리역·구리전통시장 생활권</span><span class="topic-desc">구리 중심 상권 방문 관리</span></a></li>
    <li><a href="/area/doldari-sutaek/"><span class="topic-name">돌다리사거리·수택동 생활권</span><span class="topic-desc">수택 상권 핵심 교차로 인근</span></a></li>
    <li><a href="/area/inchang-donggureung/"><span class="topic-name">인창동·동구릉 생활권</span><span class="topic-desc">동구릉 인접 주거 생활권</span></a></li>
    <li><a href="/area/galmae-newtown/"><span class="topic-name">갈매신도시 생활권</span><span class="topic-desc">갈매역·별내 인접 신도시 단지</span></a></li>
    <li><a href="/area/jangja-lake-park-topyeong/"><span class="topic-name">장자호수공원·토평 생활권</span><span class="topic-desc">수택동 인접 공원·주거권</span></a></li>
    <li><a href="/area/gyomun-cityhall/"><span class="topic-name">교문동·구리시청 생활권</span><span class="topic-desc">구리 행정 중심 거점</span></a></li>
    <li><a href="/area/achasan-acheon/"><span class="topic-name">아차산·아천 인접 생활권</span><span class="topic-desc">아차산 자락 인접 이동 기준</span></a></li>
    <li><a href="/area/wangsukcheon-sutaek/"><span class="topic-name">왕숙천·수택 인접 생활권</span><span class="topic-desc">왕숙천 하천변 주거 생활권</span></a></li>
    <li><a href="/area/dasan-guri-nearby/"><span class="topic-name">다산·구리 인접 생활권</span><span class="topic-desc">다산신도시 경계 인접권</span></a></li>
  </ul>
</div>
<p>지역 전체 목록은 <a href="/region/">구리시 지역별 안내</a>, 역 기준 전체는 <a href="/station/">구리시 역세권 안내</a>, 거점 기준 전체는 <a href="/area/">구리시 생활권 안내</a>에서 한눈에 비교하실 수 있습니다.</p>
</section>

<section id="check">
<h2>구리시 홈타이 예약 전 확인사항</h2>
<p>구리시 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 원활한 방문을 위해 정확한 도로명 주소, 공동현관 출입 방법, 매트를 펼 수 있는 공간, 조용한 환경을 미리 확인해 주시면 좋습니다. 구리역과 수택동처럼 접근성이 좋은 지역도 있지만, 동구동 사노동 방면이나 아천동 일부는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 방문 전 준비사항은 <a href="/guide/">이용 전 확인사항</a>에, 출장마사지와 홈타이의 차이와 이용 기준은 <a href="/hometai-guide/">홈타이 이용 가이드</a>에 정리했습니다.</p>
</section>

<section id="dedupe">
<h2>구리시 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 검색 순위를 노린 대량 저가치 페이지를 만들지 않습니다. 교문1·2동, 수택1·2·3동을 각각 만들지 않고 대표동으로 통합하며, 사노동·토평동·아천동은 단독 얇은 페이지 대신 생활권 페이지에서 보조 설명합니다. 구리역 페이지와 인창동 페이지, 장자호수공원역 페이지와 수택동 페이지는 같은 본문을 쓰지 않고 역세권 기준과 지역 기준으로 역할을 나눕니다. 지역명만 바꿔 같은 문장을 반복하는 방식은 사용하지 않으며, 비용과 절차는 화면에 적힌 그대로 상담에서 안내합니다. 운영 주체와 콘텐츠 작성·검수 방식은 <a href="/about/">사이트 소개</a>에서 공개합니다.</p>
</section>

<section id="how-to-use">
<h2>구리시 출장마사지 사이트 이용 방법</h2>
<p>먼저 거주하시거나 머무시는 위치를 대표동, 역세권, 생활권 중 익숙한 기준으로 찾으신 뒤, 해당 페이지에서 방문 가능 지역과 예약 전 확인사항을 확인하세요. 그다음 <a href="/reservation/">예약 안내</a>에서 가능 시간과 결제·취소 기준을 보시고, 전화로 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다. 어느 기준으로 들어오셔도 예약 절차와 비용 기준은 동일하니, 본인에게 편한 기준으로 보시면 됩니다.</p>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>구리시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "구리시 출장마사지｜구리역·갈매·인창·수택 홈타이 지역 안내",
    "desc": "구리시 출장마사지·홈타이 예약 전 구리역, 갈매동, 인창동, 교문동, 수택동 생활권을 확인하세요.",
    "h1": "구리시 출장마사지 · 구리시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
