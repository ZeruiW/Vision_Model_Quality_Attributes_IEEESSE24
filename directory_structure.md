/data/
│
├── /datasets/
│   ├── /imagenet/
│   │   ├── /original/             
│   │   │   ├── /label1/
│   │   │   ├── /label2/
│   │   │   └── ...
│   │   └── /adversarials/         
│   │       ├── /gaussian_noise/
│   │       │   ├── /1/
│   │       │   ├── /2/
│   │       │   └── ...
│   │       ├── /shot_noise/
│   │       │   ├── /1/
│   │       │   └── ...
│   │       ├── /impulse_noise/
│   │       │   ├── /1/
│   │       │   └── ...
│   │       ├── /defocus_blur/
│   │       │   ├── /1/
│   │       │   └── ...
│   │       └── ...
│
│
├── /model_results/
│   ├── /ViT/
│   ├── /SwinTransformer/
│   └── ...
│
├── /xai_results/
│   ├── /original/
│   │   ├── /ViT/
│   │   │   ├── /gradcam/
│   │   │   ├── /method2/
│   │   │   └── ...
│   │   ├── /SwinTransformer/
│   │   │   ├── /gradcam/
│   │   │   ├── /method2/
│   │   │   └── ...
│   │   └── ...
│   ├── /adversarials/
│   │   ├── /gaussian_noise/
│   │   │   ├── /1/
│   │   │   │   ├── /ViT/
│   │   │   │   │   ├── /gradcam/
│   │   │   │   │   ├── /method2/
│   │   │   │   │   └── ...
│   │   │   │   ├── /SwinTransformer/
│   │   │   │   │   ├── /gradcam/
│   │   │   │   │   ├── /method2/
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   │   │   ├── /2/
│   │   │   └── ...
│   │   ├── /shot_noise/
│   │   │   ├── /1/
│   │   │   ├── /2/
│   │   │   └── ...
│   │   ├── /impulse_noise/
│   │   │   ├── /1/
│   │   │   ├── /2/
│   │   │   └── ...
│   │   └── ...

│
├── /evaluation_results/
│   ├── /computational_overhead/  
│   │   ├── /original/
│   │   │   ├── /ViT/
│   │   │   ├── /SwinTransformer/
│   │   │   └── ...
│   │   ├── /adversarials/
│   │   │   ├── /gaussian_noise/
│   │   │   │   ├── /1/
│   │   │   │   │   ├── /ViT/
│   │   │   │   │   ├── /SwinTransformer/
│   │   │   │   │   └── ...
│   │   │   │   ├── /2/
│   │   │   │   └── ...
│   │   │   ├── /shot_noise/
│   │   │   └── ...
│   │   └── ...
│   ├── /prediction_changes/      
│   │   ├── /original/
│   │   │   ├── /ViT/
│   │   │   ├── /SwinTransformer/
│   │   │   └── ...
│   │   ├── /adversarials/
│   │   │   ├── /gaussian_noise/
│   │   │   │   ├── /1/
│   │   │   │   │   ├── /ViT/
│   │   │   │   │   ├── /SwinTransformer/
│   │   │   │   │   └── ...
│   │   │   │   ├── /2/
│   │   │   │   └── ...
│   │   │   ├── /shot_noise/
│   │   │   └── ...
│   │   └── ...
│   └── /resilience/               
│       ├── /original/
│       │   ├── /ViT/
│       │   ├── /SwinTransformer/
│       │   └── ...
│       ├── /adversarials/
│       │   ├── /gaussian_noise/
│       │   │   ├── /1/
│       │   │   │   ├── /ViT/
│       │   │   │   │   ├── /gradcam/
│       │   │   │   │   ├── /method2/
│       │   │   │   │   └── ...
│       │   │   │   ├── /SwinTransformer/
│       │   │   │   └── ...
│       │   │   ├── /2/
│       │   │   └── ...
│       │   ├── /shot_noise/
│       │   └── ...
│       └── ...
