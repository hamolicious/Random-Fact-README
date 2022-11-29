from time import gmtime

def get_current_log_time() -> str:
	ct = gmtime()
	return f'{ct.tm_mday:02}/{ct.tm_mon:02}/{ct.tm_year}  {ct.tm_hour:02}:{ct.tm_min:02}:{ct.tm_sec:02}'


