import numpy as np

def trials(td, options):
    
    """
    Function to return boolean selection of trials

    Parameters
    ----------
    td - the scipy session data
    options - dictionary of trial selection criteria
        

    Returns
    -------
    trialList: An boolean of trials to use
    """
    
    # trial outcome
    outcome = np.ravel(td['trialOutcome'])
    outcome = np.concatenate(outcome)
    
    # Create a boolean of all true the length of the trials
    trialList = np.ones((outcome.shape[0]), dtype=bool)
    
    
    outcomeList = np.zeros((outcome.shape[0]), dtype=bool)
    for iOutcome in options['trialOutcome']:
        outcomeList = np.logical_or(outcomeList, outcome == iOutcome)
        
    trialList = np.logical_and(trialList, outcomeList)
    return trialList
