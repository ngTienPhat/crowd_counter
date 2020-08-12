from config import C as cfg


def main():
    config_file = "crowd_counter/pipelines/test_config.yaml"
    cfg.merge_from_file(config_file)

    print(cfg.MODEL.TYPE)
    print(cfg.MODEL.PACKAGE)
    print(cfg.MODEL.MODULE)
    print(cfg.DATASET.TRAIN)

if __name__ == "__main__":
    main()