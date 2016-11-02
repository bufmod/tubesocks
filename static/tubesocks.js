connection = new WebSocket("ws://192.168.1.130/ws");
connection.onopen = function () {
    console.log("Websocket connected...");
    connection.send("init");
};
connection.onmessage = function (message) {
    console.log(message.data);
    var update = JSON.parse(message.data);
    $$(update.id).setValue(update.data);
};

webix.ui({container: "content",
    cols:[
        {rows:[
            {view: "template", type: "header", container: "title", template: "Input Synchronization Using Cherrypy, " +
            "Websockets (ws4py), and Webix"},
            {view: "template", type: "section", container: "title", template: "Sliders"},
            {view: "slider", id: "slider1", min:10, max: 120},
            {view: "slider", id: "slider2", min:10, max: 120},
            {view: "template", type: "section", container: "title", template: "Forms"},
            {view: "text", label: "Type some stuff:", labelWidth: 120, id: "text1"}
        ]}
    ]
});
$$("slider1").attachEvent("onItemClick", function(id, e){
    send_message(id, this.getValue(), connection);
});
$$("slider1").attachEvent("onSliderDrag", function(){
    send_message(this.config.id, this.getValue(), connection);
});
$$("slider2").attachEvent("onItemClick", function(id, e){
    send_message(id, this.getValue(), connection);
});
$$("slider2").attachEvent("onSliderDrag", function(){
    send_message(this.config.id, this.getValue(), connection);
});
$$("text1").attachEvent("onChange", function(data){
   send_message(this.config.id, data, connection) ;
});

function send_message(id, data, connection) {
    var message = {
        id: id,
        data: data
    };
    connection.send(JSON.stringify(message));
}