interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}


Array.prototype.groupBy = function (fn) {
    let obj = {}
    this.forEach(elem => {
        const key = fn(elem);
        obj[key] ? obj[key].push(elem) : obj[key] = [elem]
    })
    return obj
}