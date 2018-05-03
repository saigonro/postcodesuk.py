import re

def format_and_validate_post_codes_uk(the_post_code):

	pattern_to_match = r"^[a-zA-Z]{1,2}[0-9]{1,2}[a-zA-Z]{0,1} [0-9][a-zA-Z]{2}$"

	if re.match(pattern_to_match, the_post_code):
		correct_code = the_post_code.upper()
		return correct_code

	else:
		error_code = the_post_code
		return error_code
