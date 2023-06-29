def main(val_1, val_2, op):
    print("Operation: {} {} {} ".format(val_1, op, val_2))
  
    if op == '/':
        return(val_1 / val_2)
    elif op == '*':
        return(val_1 * val_2)
    elif op == '+':
        return(val_1 + val_2)
    elif op == '-':
        return(val_1 - val_2)
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # path from where to load the data
    parser.add_argument('--v1', type=int, required=True)
    parser.add_argument('--v2', type=int, required=True)
    # indicate operation to perform
    parser.add_argument('--op', type=str, choices=['/', '*', '+', '-'], default='+')

    args = parser.parse_args()

    value_1 = args.v1
    value_2 = args.v2
    operation = args.op
    
    # load the data
    result = main(value_1, value_2, operation)
    
    #data.to_csv("preprocessed_data/data.csv", index=False)
    #clean_data.to_csv("preprocessed_data/clean_data.csv", index=False)
    #np.save("preprocessed_data/corpus", np.array(corpus, dtype=object))