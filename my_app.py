import hydra
from omegaconf import DictConfig, OmegaConf
from haystack.components.generators.chat import OpenAIChatGenerator
from dotenv import load_dotenv
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret
load_dotenv()

@hydra.main(config_path="conf", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:
    print("My Config:")
    cfg = OmegaConf.to_object(cfg)
    print(cfg)
    cfg['generator']['api_key'] = Secret.from_token(cfg['generator']['api_key'])
    client = OpenAIChatGenerator(**cfg['generator'])
    output = client.run([ChatMessage.from_user(cfg['query'])])

    print(output['replies'][0].text)

if __name__ == "__main__":
    main()