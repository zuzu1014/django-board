$(document).ready(function() {
    const attachInfiniteScroll = (sentinel, scrollElement) => {

        console.log("attachInfiniteScroll이 시작")
            //
        let counter = 1;
        let end = false;
        let observer = new IntersectionObserver(async(entries) => {
            let bottomEntry = entries[0];
            if (!end && bottomEntry.intersectionRatio > 0) {
                $.ajax({
                    type: "POST",
                    dataType: "json",
                    data: {
                        "counter": counter,
                        'csrfmiddlewaretoken': '{{ csrf_token }}'
                    },
                    url: "{% url 'posts:board-scroll' %}",
                    success: function(response) {
                        if (response.msg == "success") {
                            counter = Number(response.counter)
                            console.log(typeof counter)
                        } else {
                            end = true;
                        }
                    },
                    error: function() {
                        console.log(error)
                    }
                }).then(() => {
                    counter += 1;
                })
            }
        })
        observer.observe(sentinel);
    };
    let sentiner = document.querySelector("#sentinel")
    let scrollElement = document.querySelector("#board")
    attachInfiniteScroll(sentiner, scrollElement);
})