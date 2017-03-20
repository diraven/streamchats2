window.chats = [];
// TODO: Make this generated template instead of raw static and add translation

function reloadChats() {
	$.ajax({
		url: "/chats/ajax/list"
	}).done(function (data) {
		$('.jsPanel .chat').closest('.jsPanel').remove();
		$.each(data['data'], function (i, v) {
			loadChat(v['id']);
			//window.chats[v['id']] = $.jsPanel({
			//	id: "chat_" + v['id'],
			//	title: v['provider_title'] + " (" + v['identifier'] + ")",
			//	position: {top: v['top'], left: v['left']},
			//	size: {width: v['width'], height: v['height']},
			//	content: v['code'],
			//	addClass: {
			//		content: "chat"
			//	}
			//});
		});
	});
}

function reloadChat(id) {
	unloadChat(id);
	loadChat(id);
}

function unloadChat(id) {
	$('#chat_' + id).remove();
	delete window.chats[id];
}

function getNumericId(id) {
	return id.replace('chat_', '');
}

function loadChat(id) {
	$.ajax({
		url: "/chats/ajax/get",
		data: {id: id}
	}).done(function (data) {
		var v = data['data'];
		window.chats[v['id']] = $.jsPanel({
			id: "chat_" + v['id'],
			title: v['provider_title'] + " (" + v['identifier'] + ")",
			position: {top: v['top'], left: v['left']},
			size: {width: v['width'], height: v['height']},
			content: v['code'],
			addClass: {
				content: "chat"
			},
			callback: function (jspanel) {
				if (v['status'] == 'normalized') {
					jspanel.normalize();
				}
				else if (v['status'] == 'maximized') {
					jspanel.maximize();
				}
				else if (v['status'] == 'minimized') {
					jspanel.minimize();
				}
				else if (v['status'] == 'smallified') {
					jspanel.smallify();
				}
			}
		});
	});
}

function saveChatStatus(id, status) {
	$.ajax({
		url: "/chats/ajax/set",
		data: {
			id: getNumericId(id),
			status: status
		}
	}).done(function (data) {
		if (data['success'] == false) {
			alert(data['message']);
			return false;
		}
	});
}

function isChatPanel(id) {
	return (id.indexOf("chat_") == 0)
}

// Core functionality
$(function () {
	// jsPanel defaults
	$.jsPanel.defaults.bootstrap = 'default';
	$.jsPanel.defaults.selector = '#objects';
	$.jsPanel.defaults.draggable = {
		start: function (event, ui) {
			$('iframe').css('pointer-events', 'none');
		},
		stop: function (event, ui) {
			$('iframe').css('pointer-events', 'auto');
			$.ajax({
				url: "/chats/ajax/set",
				data: {
					id: getNumericId($(ui.helper).closest('.jsPanel').attr('id')),
					top: ui.position.top,
					left: ui.position.left
				}
			}).done(function (data) {
				if (data['success'] == false) {
					alert(data['message']);
					return false;
				}
			});
		}
	};
	$.jsPanel.defaults.resizable = {
		handles: "e, s, se",
		autoHide: false,
		//minWidth: 150,
		//minHeight: 100,
		start: function (event, ui) {
			$('iframe').css('pointer-events', 'none');
		},
		stop: function (event, ui) {
			$('iframe').css('pointer-events', 'auto');
			$.ajax({
				url: "/chats/ajax/set",
				data: {
					id: getNumericId($(ui.helper).closest('.jsPanel').attr('id')),
					width: ui.size.width,
					height: ui.size.height
				}
			}).done(function (data) {
				if (data['success'] == false) {
					alert(data['message']);
					return false;
				}
			});
		}
	};
	// On jsPanel close - remove chat
	$("body")
		.on("jspanelclosed", function closeHandler(event, id) {
			if (isChatPanel(id)) {
				$.ajax({
					url: "/chats/ajax/delete",
					data: {
						id: getNumericId(id)
					}
				}).done(function (data) {
					if (data['success'] == false) {
						alert(data['message']);
						return false;
					}
				});
			}
		})
		.on("jspanelminimized", function (event, id) {
			if (isChatPanel(id)) {
				saveChatStatus(id, 'minimized');
			}
		})
		.on("jspanelmaximized", function (event, id) {
			if (isChatPanel(id)) {
				saveChatStatus(id, 'maximized');
			}
		})
		.on("jspanelsmallified", function (event, id) {
			if (isChatPanel(id)) {
				saveChatStatus(id, 'smallified');
			}
		})
		.on("jspanelnormalized", function (event, id) {
			if (isChatPanel(id)) {
				saveChatStatus(id, 'normalized');
			}
		});

	// On new chat click open "new chat" jspanel
	$(function () {
		$('#chat_add').click(function () {
			window.last_modal = $.jsPanel({
				id: "panel_chat_new",
				bootstrap: "default",
				title: "Add chat",
				position: "center",
				size: "auto",
				paneltype: {
					type: 'modal',
					mode: 'default'
				},
				ajax: {
					url: "/chats/ajax/new",
					done: function (data, textStatus, jqXHR, jsPanel) {
						jsPanel.content.prepend(data['data']);
					}
				}
			});
		});
	});

	// News processing
	$(function () {
		$.ajax({
			url: "/ajax/get_news"
		}).done(function (data) {
			if (data['success'] == false) {
				alert(data['message']);
				return false;
			}
			$.each(data['data'], function (k, v) {
				noty({
					text: v['date'] + '<br>' + '<h3>' + v['title'] + '</h3>' + v['text'],
					layout: 'topLeft',
					closeWith: ['button'],
					type: v['type'],
					maxVisible: 1,
					callback: {
						onClose: function () {
							$.ajax({
								url: "/ajax/set_news_read",
								data: {id: k}
							}).done(function (data) {
								if (data['success'] == false) {
									alert(data['message']);
									return false;
								}
							});
						}
					}
				});
			});
		});
	});

	reloadChats();
});