podcasts = [
    ['Build Your Own Website, No Coding Required! - with Strikingly CEO David Chen', 'August 28, 2017', 340433384],
    ['The Modularization of Real-Time Communication - with Agora.io CEO Tony Zhao','August 25, 2017', 339386933],
    ["The Do's and Do Not's of China Market Entry - with O'Melveny Managing Partner Walker Wallace",'August 14, 2017', 338120868],
    ['"Rent-to-Buy" the Chinese Runway - with YCloset COO Michael Wang','August 3, 2017',337946870],
    ['A Gradual, Evolutionary Approach to Disrupting Education - with 17zuoye Cofounder Dun Xiao','July 20, 2017',337946548],
    ['From Silicon Valley to China to India - with Xiaomi Global Head of Sales & Ops Alvin Tse','July 1, 2017',337946552],
    ["Tackling China's Pollution Problem One Solar Panel at a Time - with Xiaosolar CEO Henry Yin","June 29, 2017",337945539],
    ['Introducing the Personal Robot - with Ninebot VP of Robotics Li Pu','June 29, 2017',337945843],
    ['From Sequoia to Democratizing Consumer Finance For the Underserved - with Omni Prime CEO Dan Hu','June 20, 2017',337946531],
    ['Successfully Launching Chinese Start Ups as an Expat - with Vericant CEO Guy Sivan','June 20, 2017',337945770],
    ['Exporting Chinese Business Models: Ofo, Xiaomi, and Beyond - with Shunwei Partner Tian Cheng','June 20, 2017',337945358],
    ["What's Different About China's Tech Scene and How Are They Innovating? - with Shunwei VP Meng Xing","June 19, 2017",337945209],
    ['The Boom Bust Chinese Sharing Economy - with Woo Space CEO Randy Wan','June 17, 2017',337945462],
]

key_podcastId = '#podcastId#'
key_title = '#podcastTitle#'
key_date = '#podcastDate#'
template = '<div id="'+key_podcastId+'" style="margin-bottom: 2.5em"><div style="font-size: 26px;margin-bottom: 5px;line-height: 1.2;font-family: cardo, georgia, serif;color: #555;text-align:left;"><a style="border-bottom:none;">'+key_title+'</a></div><div style="margin-bottom:5px;font-size: 83%;line-height: 1.5;text-align: left;font-weight: inherit;font-family: helvetica, sans-serif;"><span>'+key_date+'</span></div><iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/'+key_podcastId+'&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe></div>'
outputHTML = ''

for podcast in podcasts:
    podcast_id = podcast[2]
    title = podcast[0]
    date = podcast[1]
    current_HTML = template.replace(key_podcastId, str(podcast_id))
    current_HTML = current_HTML.replace(key_title, title)
    current_HTML = current_HTML.replace(key_date, date)
    outputHTML = outputHTML + current_HTML
file = open('output.html', 'w')
file.write(outputHTML)
file.close()


