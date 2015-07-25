import i3

outputs = [output for output in i3.get_outputs() if output['active']]

workspaces = i3.get_workspaces()

if len(outputs) == 2:
    for workspace in workspaces:
        print(workspace['name'])
        i3.workspace(workspace['name'])
        i3.command('move', 'workspace to output right')
