def apply_field_mapping(instance_config, issue):
    # Placeholder for field mapping logic
    pass

def apply_value_mapping(instance_config, field, value):
    value_map = instance_config['value_mapping'].get(field, {})
    return value_map.get(value, value)  # Return the mapped value or the original if no mapping exists

