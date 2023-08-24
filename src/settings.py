from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "MVTec D2S"
PROJECT_NAME_FULL: Optional[str] = "MVTec D2S: MVTec D2S Densely Segmented Supermarket Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.BY_NC_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Retail()]
CATEGORY: Category = Category.Retail()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [
    AnnotationType.InstanceSegmentation(),
    AnnotationType.ObjectDetection(),
]

RELEASE_DATE: Optional[str] = "2018-04-23"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://www.mvtec.com/company/research/datasets/mvtec-d2s"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1811026
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/mvtec-d2s"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.mvtec.com/company/research/datasets/mvtec-d2s"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "adelholzener_alpenquelle_classic": [230, 25, 75],
    "adelholzener_alpenquelle_classic_bbox": [230, 25, 75],
    "adelholzener_alpenquelle_naturell": [60, 180, 75],
    "adelholzener_alpenquelle_naturell_bbox": [60, 180, 75],
    "adelholzener_classic_bio_apfelschorle_02": [255, 225, 25],
    "adelholzener_classic_bio_apfelschorle_02_bbox": [255, 225, 25],
    "adelholzener_classic_naturell": [0, 130, 200],
    "adelholzener_classic_naturell_bbox": [0, 130, 200],
    "adelholzener_gourmet_mineralwasser_02": [245, 130, 48],
    "adelholzener_gourmet_mineralwasser_02_bbox": [245, 130, 48],
    "augustiner_lagerbraeu_hell_05": [145, 30, 180],
    "augustiner_lagerbraeu_hell_05_bbox": [145, 30, 180],
    "augustiner_weissbier_05": [70, 240, 240],
    "augustiner_weissbier_05_bbox": [70, 240, 240],
    "coca_cola_05": [240, 50, 230],
    "coca_cola_05_bbox": [240, 50, 230],
    "coca_cola_light_05": [210, 245, 60],
    "coca_cola_light_05_bbox": [210, 245, 60],
    "suntory_gokuri_limonade": [250, 190, 212],
    "suntory_gokuri_limonade_bbox": [250, 190, 212],
    "tegernseer_hell_03": [0, 128, 128],
    "tegernseer_hell_03_bbox": [0, 128, 128],
    "corny_nussvoll": [220, 190, 255],
    "corny_nussvoll_bbox": [220, 190, 255],
    "corny_nussvoll_single": [170, 110, 40],
    "corny_nussvoll_single_bbox": [170, 110, 40],
    "corny_schoko_banane": [255, 250, 200],
    "corny_schoko_banane_bbox": [255, 250, 200],
    "corny_schoko_banane_single": [128, 0, 0],
    "corny_schoko_banane_single_bbox": [128, 0, 0],
    "dr_oetker_vitalis_knuspermuesli_klassisch": [170, 255, 195],
    "dr_oetker_vitalis_knuspermuesli_klassisch_bbox": [170, 255, 195],
    "koelln_muesli_fruechte": [128, 128, 0],
    "koelln_muesli_fruechte_bbox": [128, 128, 0],
    "koelln_muesli_schoko": [255, 215, 180],
    "koelln_muesli_schoko_bbox": [255, 215, 180],
    "caona_kakaohaltiges_getraenkepulver": [0, 0, 128],
    "caona_kakaohaltiges_getraenkepulver_bbox": [0, 0, 128],
    "cocoba_fruehstueckskakao_mit_honig": [128, 128, 128],
    "cocoba_fruehstueckskakao_mit_honig_bbox": [128, 128, 128],
    "cafe_wunderbar_espresso": [230, 25, 75],
    "cafe_wunderbar_espresso_bbox": [230, 25, 75],
    "douwe_egberts_professional_kaffee_gemahlen": [60, 180, 75],
    "douwe_egberts_professional_kaffee_gemahlen_bbox": [60, 180, 75],
    "gepa_bio_caffe_crema": [255, 225, 25],
    "gepa_bio_caffe_crema_bbox": [255, 225, 25],
    "gepa_italienischer_bio_espresso": [0, 130, 200],
    "gepa_italienischer_bio_espresso_bbox": [0, 130, 200],
    "apple_braeburn_bundle": [245, 130, 48],
    "apple_braeburn_bundle_bbox": [245, 130, 48],
    "apple_golden_delicious": [145, 30, 180],
    "apple_golden_delicious_bbox": [145, 30, 180],
    "apple_granny_smith": [70, 240, 240],
    "apple_granny_smith_bbox": [70, 240, 240],
    "apple_red_boskoop": [240, 50, 230],
    "apple_red_boskoop_bbox": [240, 50, 230],
    "avocado": [210, 245, 60],
    "avocado_bbox": [210, 245, 60],
    "banana_bundle": [250, 190, 212],
    "banana_bundle_bbox": [250, 190, 212],
    "banana_single": [0, 128, 128],
    "banana_single_bbox": [0, 128, 128],
    "clementine": [220, 190, 255],
    "clementine_bbox": [220, 190, 255],
    "clementine_single": [170, 110, 40],
    "clementine_single_bbox": [170, 110, 40],
    "grapes_green_sugraone_seedless": [255, 250, 200],
    "grapes_green_sugraone_seedless_bbox": [255, 250, 200],
    "grapes_sweet_celebration_seedless": [128, 0, 0],
    "grapes_sweet_celebration_seedless_bbox": [128, 0, 0],
    "kiwi": [170, 255, 195],
    "kiwi_bbox": [170, 255, 195],
    "orange_single": [128, 128, 0],
    "orange_single_bbox": [128, 128, 0],
    "oranges": [255, 215, 180],
    "oranges_bbox": [255, 215, 180],
    "pear": [0, 0, 128],
    "pear_bbox": [0, 0, 128],
    "pasta_reggia_elicoidali": [128, 128, 128],
    "pasta_reggia_elicoidali_bbox": [128, 128, 128],
    "pasta_reggia_fusilli": [230, 25, 75],
    "pasta_reggia_fusilli_bbox": [230, 25, 75],
    "pasta_reggia_spaghetti": [60, 180, 75],
    "pasta_reggia_spaghetti_bbox": [60, 180, 75],
    "franken_tafelreiniger": [255, 225, 25],
    "franken_tafelreiniger_bbox": [255, 225, 25],
    "pelikan_tintenpatrone_canon": [0, 130, 200],
    "pelikan_tintenpatrone_canon_bbox": [0, 130, 200],
    "ethiquable_gruener_tee_ceylon": [245, 130, 48],
    "ethiquable_gruener_tee_ceylon_bbox": [245, 130, 48],
    "gepa_bio_und_fair_fencheltee": [145, 30, 180],
    "gepa_bio_und_fair_fencheltee_bbox": [145, 30, 180],
    "gepa_bio_und_fair_kamillentee": [70, 240, 240],
    "gepa_bio_und_fair_kamillentee_bbox": [70, 240, 240],
    "gepa_bio_und_fair_kraeuterteemischung": [240, 50, 230],
    "gepa_bio_und_fair_kraeuterteemischung_bbox": [240, 50, 230],
    "gepa_bio_und_fair_pfefferminztee": [210, 245, 60],
    "gepa_bio_und_fair_pfefferminztee_bbox": [210, 245, 60],
    "gepa_bio_und_fair_rooibostee": [250, 190, 212],
    "gepa_bio_und_fair_rooibostee_bbox": [250, 190, 212],
    "kilimanjaro_tea_earl_grey": [0, 128, 128],
    "kilimanjaro_tea_earl_grey_bbox": [0, 128, 128],
    "cucumber": [220, 190, 255],
    "cucumber_bbox": [220, 190, 255],
    "carrot": [170, 110, 40],
    "carrot_bbox": [170, 110, 40],
    "feldsalat": [255, 250, 200],
    "feldsalat_bbox": [255, 250, 200],
    "lettuce": [128, 0, 0],
    "lettuce_bbox": [128, 0, 0],
    "rucola": [255, 215, 180],
    "rucola_bbox": [255, 215, 180],
    "salad_iceberg": [0, 0, 128],
    "salad_iceberg_bbox": [0, 0, 128],
    "zucchini": [128, 128, 128],
    "zucchini_bbox": [128, 128, 128],
    "suntory_gokuri_lemonade": [230, 25, 75],
    "suntory_gokuri_lemonade_bbox": [230, 25, 75],
    "caona_cocoa": [60, 180, 75],
    "caona_cocoa_bbox": [60, 180, 75],
    "douwe_egberts_professional_ground_coffee": [255, 225, 25],
    "douwe_egberts_professional_ground_coffee_bbox": [255, 225, 25],
    "cocoba_cocoa": [0, 130, 200],
    "cocoba_cocoa_bbox": [0, 130, 200],
    "corn_salad": [245, 130, 48],
    "corn_salad_bbox": [245, 130, 48],
    "rocket": [145, 30, 180],
    "rocket_bbox": [145, 30, 180],
    "vine_tomatoes": [70, 240, 240],
    "vine_tomatoes_bbox": [70, 240, 240],
    "roma_vine_tomatoes": [240, 50, 230],
    "roma_vine_tomatoes_bbox": [240, 50, 230],
    "adelholzener_alpenquelle_classic_075": [210, 245, 60],
    "adelholzener_alpenquelle_classic_075_bbox": [210, 245, 60],
    "adelholzener_alpenquelle_naturell_075": [250, 190, 212],
    "adelholzener_alpenquelle_naturell_075_bbox": [250, 190, 212],
    "adelholzener_classic_naturell_02": [0, 128, 128],
    "adelholzener_classic_naturell_02_bbox": [0, 128, 128],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/pdf/1804.08292.pdf"
CITATION_URL: Optional[str] = "https://www.mvtec.com/company/research/datasets/mvtec-d2s"
AUTHORS: Optional[List[str]] = [
    "Patrick Follmann",
    "Tobias Böttger",
    "Philipp Härtinger",
    "Rebecca König",
    "Markus Ulrich",
]


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "MVTec Software GmbH, Germany",
    "Technical University of Munich",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.mvtec.com/company/research",
    "https://www.tum.de/en/",
]
SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    '*train* ablation studies': ['rot0', 'light0', "rot0_light0"],
    '*validation* specific difficulties': ['random_background_wo_clutter', 'wo_occlusion', 'clutter', 'random_background', 'occlusion'],
    '*test* specific difficulties': ['info_clutter', 'info_occlusion', 'info_random_background_wo_clutter', 'info_random_background', 'info', 'info_wo_occlusion' ],
}

TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
