import langdetect
from deep_translator import GoogleTranslator
import logging

def translate_german_parts(input_file, output_file):
    """
    Translates German parts of a text file to English.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """

    logging.basicConfig(filename='translation.log', level=logging.INFO)

    try:
        with open(input_file, 'r', encoding='utf-8') as input_fp, open(output_file, 'w', encoding='utf-8') as output_fp:
            for line in input_fp:
                line = line.strip()
                try:
                    lang = langdetect.detect(line)
                    if lang == 'de':
                        translation = GoogleTranslator(source='de', target='en').translate(line)
                        output_fp.write(translation + '\n')
                    else:
                        output_fp.write(line + '\n')
                except langdetect.LangDetectException as e:
                    logging.error(f"Language detection failed for line: {line}, Error: {e}")
                except Exception as e:
                    logging.error(f"An error occurred: {e}")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")

# Example usage:
input_file_path = "/Users/neo/Desktop/test/AUSYT_FULL_SUBTITLES.srt"
output_file_path = "/Users/neo/Desktop/test/translated_output.srt"
translate_german_parts(input_file_path, output_file_path)
