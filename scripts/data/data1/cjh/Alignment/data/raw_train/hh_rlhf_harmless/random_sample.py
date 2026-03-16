#!/usr/bin/env python
import json
import random
import argparse
import math
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True, help="输入文件")
    parser.add_argument("--output_file", type=str, required=True, help="输出文件")
    parser.add_argument("--rate", type=int, default=0.15, help="抽取数量")
    parser.add_argument("--seed", type=int, default=42, help="随机种子")
    args = parser.parse_args()

    # 设置随机种子
    random.seed(args.seed)
    
    # 读取所有数据
    print(f"读取文件: {args.input_file}")
    data = []
    with open(args.input_file, 'r') as f:
        for line in f:
            data.append(line.strip())
    
    print(f"总数据量: {len(data)} 条")
    
    # 随机抽取
    sample_size = min(math.floor(args.rate*len(data)), len(data))
    sampled_data = random.sample(data, sample_size)
    
    print(f"随机抽取 {sample_size} 条")
    
    # 保存
    with open(args.output_file, 'w') as f:
        for line in sampled_data:
            f.write(line + '\n')
    
    print(f"已保存到: {args.output_file}")
    
    # 显示前几条示例
    print("\n前3条示例:")
    for i, line in enumerate(sampled_data[:3]):
        item = json.loads(line)
        print(f"{i+1}. 用户: {item['messages'][0]['content'][:50]}...")

if __name__ == "__main__":
    main()