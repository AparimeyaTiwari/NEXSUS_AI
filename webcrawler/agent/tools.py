# agent/tools.py
from core.verification_engine import verify_person
from crawler.crawler import crawl_web
from npi_verifier.npi_lookup import verify_npi
from agent.extrainfo_agent import run_extrainfo as fuzzy_extrainfo


def run_verify_person(name: str, npi: str = None):
    return verify_person(name, npi)

def run_npi_lookup(npi: str):
    return verify_npi(npi)

def run_crawl(name: str, max_pages: int = 5):
    return crawl_web(name, max_pages=max_pages, depth=1)

def run_extrainfo(name: str, extra_info: dict, web_results: list):
    return fuzzy_extrainfo(name, extra_info, web_results)
