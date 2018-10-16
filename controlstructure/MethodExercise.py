def taxation_method(state,gross_income):
    if state == 'sfo':
        st = 0.2
    elif state == 'ny':
        st = 0.3
    elif state == 'texas':
        st = 0.4
    state_tax = st * gross_income
    federal_tax = 0.1 * gross_income
    ni = gross_income - federal_tax - state_tax
    print('gross income is: ', gross_income)
    print('state tax for ' + state + ' = ', state_tax)
    print('federal tax = ', federal_tax)
    return(ni)

net_income = taxation_method('ny',400000)

print('Final tax for the state is ', net_income)


def taxation_method_dict(statename, grossincome):
    state_name = {'sfo': 0.2, 'ny': 0.3, 'texas': 0.4}

    federal_tax = grossincome * 0.1

    if statename in state_name:
        state_tax = state_name[statename] * grossincome
        net_tax = grossincome - (state_tax + federal_tax)
        print('final tax for ' + statename + ' is: ', net_tax)
        return (net_tax)
    else:
        print('Incorrect country')
        return None

taxation_method_dict('sfo', 400000)