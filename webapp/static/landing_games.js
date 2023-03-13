const group = document.getElementById('games_group');

const srcs = [
    '//via.placeholder.com/300x300/31f',
    '//via.placeholder.com/300x300/aba',
    '//via.placeholder.com/300x300/fc0',
    '//via.placeholder.com/300x300/e66',
    '//via.placeholder.com/300x300/7d2',
    '//via.placeholder.com/300x300',
    '//via.placeholder.com/300x300/aba',
    '//via.placeholder.com/300x300/fc0',
    '//via.placeholder.com/300x300/31f',
    '//via.placeholder.com/300x300/7d2',
    '//via.placeholder.com/300x300/e66',
    '//via.placeholder.com/300x300',
];

srcs.forEach((src) => {
    const li = document.createElement('li');
    li.setAttribute('class', 'list-group-item col-2 bg-transparent border-0');
    group.appendChild(li);

    const img = document.createElement('img');
    img.setAttribute('class', 'img-fluid rounded');
    img.setAttribute('src', src);
    li.appendChild(img);
})

window.addEventListener('load', () => {
    var last = -1;
    var goback = false;
    self.setInterval(() => {
        if (last === group.scrollLeft) {
            goback = !goback;
        }
        last = group.scrollLeft;
        if (goback) {
            group.scrollTo(group.scrollLeft - 1, 0);
        } else {
            group.scrollTo(group.scrollLeft + 1, 0);
        }
    }, 15);
  });