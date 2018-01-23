class Item(object):
	item_id = ''
	name = ''
	description = ''
	icon = '' # the class for <i>
	scale = 0. # Proficiency rank 0.0-1.0

	def __init__(self, item_id, name, icon='', description='', scale=0, scroll_bar_length=100):
		self.item_id = item_id
		self.name = name
		self.icon = icon
		self.description = description
		self.scale = scale

		self.pos = (scroll_bar_length + 1) * scale - 1.25

	def scroll_bar_html(self):
		return '<div class="project-item" id="%s" style="left: %srem">' % (self.item_id, self.pos) + \
		'<div class="project-item-icon">' + \
				'<i class="%s"></i>' % (self.icon) + \
			'</div>' + \
		'</div>'

	def item_content_title(self):
		return '<i class="%s"></i>' % self.icon

	def item_content_body_html(self):
		return '<p>%s</p>' % self.description

	def item_content_js(self):
		return '$("#%s").click(function() {' % self.item_id + \
			'$("#project-content .mdl-card__supporting-text").html("%s");' % self.description + \
			'''$("#project-content .mdl-card__title-text").html('<i class="%s"></i>');'''% self.icon + \
		'});'
		pass

