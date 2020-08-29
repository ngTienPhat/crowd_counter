import importlib
import logging

logger = logging.getLogger(__name__)

class EngineFactory(object):
    def __init__(self, config):
        """
        Args:
            config (dict)

        Example:
            >>> config = {
            ...    "human_detector": {
            ...        "package": "crowd_counter.s_dcnet.sdc_engine",
            ...        "module": "SDC_Engine",
            ...        "args": ["/path/to/weight.pth"],
            ...        "kwargs": {},
            ...    },
            ... }

            >>> # Above config means:
            >>> # from yolo import YoloModel
            >>> # model = YoloModel(*args, **kwargs)

            >>> from crow_counter.engines import EngineFactory
            >>> factory = EngineFactory(config)

            >>> model = factory.get_instance("human_detector")
        """
        self.module_dictionary = {}
        for k, v in config.items():
            module = self._load_module(v)

            if module is None:
                continue
            self.module_dictionary[k] = module

    def get_instance(self, instance_name):
        instance = self.module_dictionary(instance_name)
        if instance is None:
            logger.warning(f"Not found {instance}")

        return instance

    def _load_module(self, module_config):
        package = module_config["package"]
        module = module_config["module"]
        Module = self._get_module_class(package, module)

        if Model is None:
            return None

        args = module_config.get("args", list())
        kwargs = module_config.get("kwargs", dict())

        model = Module(*args, **kwargs)
        return model

    def _get_module_class(self, package_name, module_name):
        """ Get Module Constructor from config 
        Args:
            package_name (str): Name of package
            module_name (str): Name of Module
        Return:
            constructor (type)
        
        Note: This function act as a pseudo below:
        >>> from `package_name` import `module_name`
        >>> return `module_name`
        """

        try:
            package = importlib.import_module(module_name)
            class_ = getattr(package, class_name)

            return class_
        except ModuleNotFoundError:
            logger.error(
                f"Cannot import {module_name}, maybe corresponding package has not been installed",
                exc_info=True,
            )
        except AttributeError:
            logger.error(
                f"Cannot find class {class_name} in module {module_name}", exc_info=True
            )

        return None

