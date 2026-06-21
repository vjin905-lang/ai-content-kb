# Prompt组合规则

1. 顺序：
BASE → STYLE → CHARACTER → DETAIL → NEGATIVE

2. 冲突处理：
- style冲突时，优先character
- negative统一最后处理

3. LoRA规则：
- 同类型LoRA只允许1个主权重 > 0.6
