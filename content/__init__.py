# 전체 페이지 목록 집계 (구리시 출장마사지·홈타이)
from . import main, areas, stations, localareas, info, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + localareas.PAGES
    + info.PAGES
    + [about.PAGE]
)
