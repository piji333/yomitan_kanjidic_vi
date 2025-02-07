from src.utils.call_search_api import call_search_api


def get_am_han_viet(res):
    found_res = res[0] if res else {}
    return found_res.get("mean", "")


def get_nghia_han_viet(res):
    found_res = res[0] if res else {}
    detail = found_res.get("detail", "")
    return detail.split("##")


def update_kanji(session, kanji_obj):
    kanji = kanji_obj[0]
    res = call_search_api(session, kanji, "kanji")
    am_han_viet = get_am_han_viet(res["results"])
    nghia_han_viet = get_nghia_han_viet(res["results"])
    kanji_obj[1] = kanji_obj[1] + " " + am_han_viet
    kanji_obj[4] = kanji_obj[4] + nghia_han_viet
