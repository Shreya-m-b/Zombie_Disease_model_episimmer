from episimmer.policy import vaccination_policy
from episimmer.policy import lockdown_policy
def agents_per_step_fn(time_step):

	if(time_step%2==5 or time_step%7==6):
		return 200
	else:
		return 100


def generate_policy():
	policy_list=[]

	policy= vaccination_policy.VaccinationPolicy(agents_per_step_fn)
	vaccines_available = {
		'poweful2': {'cost': 30, 'count': 8, 'efficacy': 0.7, 'decay': [24,16], 'dose': 2, 'interval': [30]},
		'booster': {'cost': 30, 'count': 4, 'efficacy': 0.7, 'decay': [32], 'dose': 1, 'interval': []}
	}
	policy.add_vaccines(vaccines_available, 'Multi')
	policy.set_register_agent_vaccine_func(policy.multi_dose_vaccination())
	policy_list.append(policy)

	
	def lockdown_fn(time_step):
		if time_step%7 in [0,3,5]:
			return True
		return False

	policy_list.append(lockdown_policy.AgentLockdown('Blood Group',['A+'],lockdown_fn))



	return policy_list