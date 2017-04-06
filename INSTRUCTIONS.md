**YunoJuno Platform Developer Challenge**

**UPDATE** For the avoidance of any doubt, you shouldn't need to understand Trello or HipChat to solve this. The contents of the solution are in the comments below. The test itself is simple, and what we want to see is _how_ you work with an existing codebase. Code, comments, commit notes, commit contents, tests, pull requests - everything that shows us that you'll fit in with the YJ team. If in any doubt, refer to this document for more details on how we work - https://yunojuno.github.io/test-docs/contributing/.

_This challenge is a pre-requisite for anyone applying to YunoJuno for a Django-related role. It is designed to demonstrate familiarity with Git and Django, and to show how someone codes. Before reading this you should read the main repo README file for background on the project._

---

One of the events captured by the existing test_app is `addAttachmentToCard`. This event is sent to HipChat using the following template:

```html
<strong>{{action.memberCreator.initials}}</strong> added attachment "<strong>
<a href="{{action.data.attachment.url}}">{{action.data.attachment.name}}</a></strong>"
```

Which renders as:

![screen shot 2014-12-08 at 12 52 48](https://cloud.githubusercontent.com/assets/200944/5339479/43f141b4-7ed9-11e4-8188-f316ab4c7286.png)

Whilst this works for all attachment types, HipChat can display image attachments inline, within the chat, when rendered as HTML.

---

The specific challenge of this issue is to implement content-type specific rendering of the HipChat message for the `addAttachmentToCard` event. If the attachment content-type _is_ an image (e.g. 'image/png') then it should be displayed using `<a href='{{url}}'><img src={{url}}></a>`, but if it's _not_ an image it should be displayed as it is currently: `<a href='{{url}}'>{{name}}</a>`

This issue is designed to give us some insight into _how_ you work, and how well you might fit into our team, and our workflow. The solution itself is not complicated, and is spelled out in the requirements below - this is more about how you code. To quote from the [Google Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html):

> If you're editing code, take a few minutes to look at the code around you and determine its style. ... If code you add to a file looks drastically different from the existing code around it, it throws readers out of their rhythm when they go to read it. Avoid this.

The requirements are the following:

1. Add a new method to the `CallbackEvent` model to resolve attachment content type
2. Extend `action_data` JSON to include the content type of attachments when added
2. Add a custom template filter to the `test_app` to display the attachment HTML
3. Override the default `addAttachmentToCard.html` template to display the new HTML
4. Improve the overall test coverage (clue: running `tox` will show you the current coverage)

Submit your application as a pull request.

PS Bonus points for a new management command to retrospectively add the content type of all the attachments added so far.

---

As a clue to this, and to prevent anyone from getting too carried away, the canonical (YJ) solution contains:

* one new requirement
* one new template
* one new template filter
* one new method (which could be done in one line)
* one edit to an existing method
