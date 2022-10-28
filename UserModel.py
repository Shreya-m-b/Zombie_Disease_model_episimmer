import episimmer.model as model

def event_contribute_fn(agent,event_info,location,current_time_step):
	if agent.state=='Zombie':
		return 1
	if agent.state=='Bitten':
		return 0.25
	if agent.state=='Injured':
		return 0.5
	if agent.state=='Dead':
		return 0.75
	return 0

def event_receive_fn(agent,ambient_infection,event_info,location,current_time_step):
	beta=0.001
	return ambient_infection*beta


class UserModel(model.StochasticModel):
	def __init__(self):
		individual_types=['Normal','Bitten','Immune','Injured','Dead','Zombie']	
		infected_states=['Zombie']
		state_proportion={				
							'Normal':0.99,
							'Bitten':0.00,
							'Immune':0,
							'Injured':0.00,
							'Dead':0.00,
							'Zombie':0.01
						}
		model.StochasticModel.__init__(self,individual_types,infected_states,state_proportion)
		self.set_transition('Normal', 'Bitten', self.p_standard(0.1))
		self.set_transition('Bitten', 'Immune', self.p_standard(0.02))
		self.set_transition('Bitten', 'Dead', self.p_standard(0.03))
		self.set_transition('Bitten', 'Injured', self.p_standard(0.04))
		self.set_transition('Injured', 'Immune', self.p_standard(0.05))
		self.set_transition('Injured', 'Dead', self.p_standard(0.06))
		self.set_transition('Dead', 'Zombie', self.p_standard(0.07))


		self.set_event_contribution_fn(event_contribute_fn)
		self.set_event_receive_fn(event_receive_fn)

		self.name='PESUIO - Zombie Model'
