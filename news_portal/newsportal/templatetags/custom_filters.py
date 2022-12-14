from django import template


register = template.Library()


words = {
    'сон': 'с**',
    'что': 'ч**',
}

@register.filter()
def censor(txt):
    text = txt
    for word, word_change in words.items():
        text = text.replace(word, word_change)
    return text

