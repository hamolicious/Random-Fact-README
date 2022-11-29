from facts import get_fact
from readme import insert_fact
from time import gmtime, sleep
from hamconf import parse_file
from util import get_current_log_time

config = parse_file('config.hamconf')
do_at = config.get('CONFIG.run_at')
done_today = False

while True:
	sleep(30)

	ct = gmtime()
	current_time = f'{ct.tm_hour:02}:{ct.tm_min:02}'

	if current_time == do_at and done_today == False:
		print(f'{get_current_log_time()} [INFO] Generating new fact')
		fact = get_fact()
		print(f'{get_current_log_time()} [INFO] Fact generated: "{fact}"')
		print(f'{get_current_log_time()} [INFO] Committing')
		insert_fact(fact)
		print(f'{get_current_log_time()} [INFO] Done, waiting')
		done_today = True

	if current_time != do_at:
		done_today = False




