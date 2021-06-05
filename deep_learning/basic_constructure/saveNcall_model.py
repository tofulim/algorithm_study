##학습된 모델 저장하기
import os
save_folder = "/opt/ml/code/save_model"
save_path = os.path.join(save_folder, "best.pth")   # ./runs/best.pth
os.makedirs(save_folder, exist_ok=True)  

torch.save(model.state_dict(), save_path)
print(f"Model saving success at {save_path}")
print(f"Saved models : {os.listdir(save_folder)}")
##불러오기
new_model = Model()
new_model.load_state_dict(torch.load(save_path))
print(f"Model loading success from {save_path}")

##불러온 모델 확인
for (name, trained_weight), (_, saved_weight) in zip(model.named_parameters(), new_model.named_parameters()):
    is_equal = torch.equal(trained_weight, saved_weight)
    print(f"parameter {name:15} from trained model and loaded model is equal? -> {is_equal}")