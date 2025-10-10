function solution(l, r) {
    var answer = [];
    for(let i = l; i <= r; i++ ){
        const str = i.toString();
        if ([...str].every(ch => ch === '0' || ch === '5')){
            answer.push(i);
        }
    }
    return answer.length > 0 ? answer : [-1];
}