from variant_generator import (
    generate_variants, grid_search, sample_from)


SAC_KWARGS = {
    'reward_scale': grid_search([1.0, 10.0, 100.0]),
}

SQL_KWARGS = {
    'reward_scale': grid_search([1.0, 10.0, 100.0]),
}

ALGORITHM_KWARGS = {
    'SAC': SAC_KWARGS,
    'SQL': SQL_KWARGS,
}


def main():
    variant_spec = {
        'algorithm_params': {
            'type': grid_search(['SAC', 'SQL']),
            'kwargs': sample_from(lambda spec: (
                ALGORITHM_KWARGS[spec['algorithm_params']['type']]
            ))
        },

    }

    from pdb import set_trace; from pprint import pprint; set_trace()

    variants = list(generate_variants(variant_spec))

    from pdb import set_trace; from pprint import pprint; set_trace()
    pass


if __name__ == '__main__':
    main()
