def ordered_configuration(configuration: str):
    parts = configuration.split('|')
    config_map = {}
    seen_configs = set()
    seen_indices = set()

    for part in parts:
        # Validation: Must have at least 4 digits for ordinal + 10 characters for config
        if len(part) != 14 or not part[:4].isdigit() or not part[4:].isalnum():
            return ["Invalid configuration"]
        
        index = part[:4]
        config_value = part[4:]

        # Validation: ordinal index must not be "0000"
        if index == "0000":
            return ["Invalid configuration"]

        # Validation: no duplicate ordinal indices
        if index in seen_indices:
            return ["Invalid configuration"]
        seen_indices.add(index)

        # Validation: configuration value must be unique
        if config_value in seen_configs:
            return ["Invalid configuration"]
        seen_configs.add(config_value)

        config_map[int(index)] = config_value

    # Validation: indices must be a complete sequence from 1 to len(parts)
    expected_indices = set(range(1, len(parts) + 1))
    actual_indices = set(int(i) for i in seen_indices)
    if actual_indices != expected_indices:
        return ["Invalid configuration"]

    # Return configurations ordered by ordinal index
    return [config_map[i] for i in sorted(config_map)]


config1 = " 0002f7c22e7904|000176a3a4d214|000305d29f44bj"
print(ordered_configuration(config1))
# Output: ['76a3a4d214', 'f7c22e7904', '05d29f4a4b']

config2 = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"
print(ordered_configuration(config2))

config3 = "0002f7c22e7904|000376a3a4d214|0004f7c22e7904"
print(ordered_configuration(config3))
