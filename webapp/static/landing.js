const games_group = document.getElementById('games_group');
const testimonials_group = document.getElementById('testimonials_group');

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
    games_group.appendChild(li);

    const img = document.createElement('img');
    img.setAttribute('class', 'img-fluid rounded');
    img.setAttribute('src', src);
    li.appendChild(img);
});

const testimonials = [
    {text:'“We were absolutely delighted to use [this] video game concept in teaching our graduates soft skills. There are many traditional methodologies out there which focus on skills building and training but the online, video game format lend to a diverse group of students perfectly. The key point of the training was also the fact that skill development could be measured quantitatively and tracked by each individual. Overall, we had very positive experience with the methodology and noted some significant skill shifts.”', author:'Sandra H., PhD'},
    {text:'Although I am not really a gamer, I have to say I enjoyed the course a lot! I even kept playing the game after the course ended. Moreover, it really helped me to think outside the box and see life-problems in a different perspective. I would recommend it 100% :-)', author:'Maria R., PhD'},
    {text:'“Working with [it] completely changed how I am looking at video games and their potential to train us for everyday life. A lot of games include various soft skills aspects and I think that, when played mindfully and aware of the methodology, it can be profitable for employees in every area of expertise and will be a crucial part of a modern professional practice.”', author:'Sebastian G'},
    {text:'“I never believed in video games as tools to develop or increase soft skills. After I joined [this] project, I not only changed my mind, but I also enjoyed my time playing together and discussing them with my colleagues. Finding creative solutions and trying hard before giving up are only two of the soft skills I have strengthened during the courses.”', author:'Cecilia B., PhD'},
    {text:'“[This] course was a lot of fun! It was really nice to have something that is a bit different to the usual lectures. Discussing with other participants during the training sessions was very interesting as well.”', author:'Francesco, student'},
];

testimonials.forEach((testimonial) => {
    const li = document.createElement('li');
    li.setAttribute('class', 'list-group-item col-7 bg-transparent border-0 mx-4');
    testimonials_group.appendChild(li);
    const card = document.createElement('div');
    card.setAttribute('class', 'card bg-light border-0 card-shadow');
    li.appendChild(card);
    const cardbody = document.createElement('div');
    cardbody.setAttribute('class', 'card-body');
    card.appendChild(cardbody);
    const blockquote = document.createElement('blockquote');
    blockquote.setAttribute('class', 'blockquote mb-0');
    cardbody.appendChild(blockquote);
    const p = document.createElement('p');
    p.setAttribute('class', 'text-start text-primary fs-5 fw-normal');
    p.innerText = testimonial.text;
    blockquote.appendChild(p);
    const footer = document.createElement('footer');
    footer.setAttribute('class', 'text-end text-primary fs-5 fw-bold');
    footer.innerText = testimonial.author;
    blockquote.appendChild(footer);
});

window.addEventListener('load', () => {
    var games_scroll_last = -1;
    var games_scroll_goback = false;
    var testimonials_scroll_last = -1;
    var testimonials_scroll_goback = false;
    self.setInterval(() => {
        // games scroll
        if ( games_scroll_last === games_group.scrollLeft) {
            games_scroll_goback = !games_scroll_goback;
        }
        games_scroll_last = games_group.scrollLeft;
        if (games_scroll_goback) {
            games_group.scrollTo(games_group.scrollLeft - 1, 0);
        } else {
            games_group.scrollTo(games_group.scrollLeft + 1, 0);
        }
        // testimonials scroll
        if ( testimonials_scroll_last === testimonials_group.scrollLeft) {
            testimonials_scroll_goback = !testimonials_scroll_goback;
        }
        testimonials_scroll_last = testimonials_group.scrollLeft;
        if (testimonials_scroll_goback) {
            testimonials_group.scrollTo(testimonials_group.scrollLeft - 1, 0);
        } else {
            testimonials_group.scrollTo(testimonials_group.scrollLeft + 1, 0);
        }
    }, 15);
});
  