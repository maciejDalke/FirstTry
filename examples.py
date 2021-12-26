boolean_variable = True
print("boolean_variable {}".format(boolean_variable))
boolean_variable = not boolean_variable
print("boolean_variable {}".format(boolean_variable))
boolean_variable = not boolean_variable
print("boolean_variable {}".format(boolean_variable))

advantage_enable = False

advantage_setting = input("Advantage is now [{0}] want change? [yes] [y]: "
                          .format(advantage_enable and "enable" or "disable")).lower()
if advantage_setting[0] == "y":
    advantage_enable = not advantage_enable

print(advantage_setting)
print(advantage_enable)

advantage_setting = input("Advantage is now [{0}] want change? [yes] [y]: "
                          .format(advantage_enable and "enable" or "disable")).lower()
if advantage_setting[0] == "y":
    advantage_enable = not advantage_enable

print(advantage_setting)
print(advantage_enable)
