#!/usr/bin/env python3

import argparse
import logging
from googletrans import Translator
import wikipediaapi


LOGGER_NAME = 'ArmWiki'
logger = logging.getLogger(LOGGER_NAME)

def setup_logging():
    global logger
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)
    logging.addLevelName(logging.INFO,    "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR,   "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.DEBUG,   "\033[1;33m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))

    logformatter = '%(asctime)s [%(levelname)s][%(name)s] %(pathname)s:%(lineno)d %(message)s'
    loglevel = logging.INFO
    logging.basicConfig(format=logformatter, level=loglevel)
    if args.verbose:
        logger.setLevel(logging.INFO)
    if args.debug:
        logger.setLevel(logging.DEBUG)
    if args.quiet:
        logger.disabled = True


def translate_single_page():
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page("BERT_(language_model)")
    translator = Translator()
    input_text = "In the above example, we did not specify the source language. Therefore, Google Translate API tries to detect source language itself. Similarly, we did not specify any destination language as well and thus, the API translated the source language into the default language that is English. But, what if you want to specify both the source and destination languages?"
    for s in page.sections:
        result = translator.translate(s.text, src='fi', dest='hy')
        logger.info(result.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-u", "--url", help="URL to the Wikipedia page.")
    input_group.add_argument("-p", "--page",   help="Wikipedia page name.")

    parser.add_argument("-o", "--output", required=True, help="Directory to store the results.")

    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-g", "--debug", action="store_true", help="Debug message output")
    parser.add_argument("-q", "--quiet", action="store_true", help="Run quiet with no message output")
    args = parser.parse_args()

    setup_logging()
    translate_single_page()
