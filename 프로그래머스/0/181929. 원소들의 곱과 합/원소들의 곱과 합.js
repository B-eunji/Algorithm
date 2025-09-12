function solution(num_list) {
    var answer = 0;
    let sum = num_list.reduce((acc,cur) => acc + cur, 0);
    let product = num_list.reduce((acc, cur) => acc * cur, 1);
    answer = product < sum ** 2 ? 1: 0;
    return answer;
}