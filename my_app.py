import hydra
from omegaconf import DictConfig, OmegaConf
from dotenv import load_dotenv
from haystack.dataclasses import ChatMessage
from src.helpers.validate_config import HydraConfig
load_dotenv()

@hydra.main(config_path="conf", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:

    cfg = OmegaConf.to_object(cfg)
    cfg: HydraConfig = HydraConfig(**cfg)
    print("My Config with pydantic:")
    print(cfg)
    # we can directly access the fields of our hydra 
    chat_messages = [ChatMessage.from_system(cfg.prompts['system_prompt'])]
    output = cfg.generator.run(chat_messages + [ChatMessage.from_user(cfg.query)])
    print(output['replies'][0].text)

if __name__ == "__main__":
    main()