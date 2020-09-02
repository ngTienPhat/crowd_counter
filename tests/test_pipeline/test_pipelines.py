from crowd_counter.pipelines.config import C as cfg

def main():
    config_file = "crowd_counter/pipelines/test_config.yaml"
    cfg.merge_from_file(config_file)


if __name__ == "__main__":
    main()