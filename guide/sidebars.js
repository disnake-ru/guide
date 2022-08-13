// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
	guideSidebar: [
		{
			type: "doc",
			label: "Вступление",
			id: "intro",
		},
		{
			type: "category",
			label: "Предисловие",
			items: [
				"prerequisites/installing-disnake",
				"prerequisites/migrating-from-dpy",
				"prerequisites/creating-your-application",
			],
		},
		{
			type: "category",
			label: "Приступая к работе",
			items: [
				"getting-started/initial-files",
				"getting-started/creating-commands",
				"getting-started/using-cogs",
			],
		},
		{
			type: "category",
			label: "Взаимодействия",
			link: { type: "doc", id: "interactions/intro" },
			items: [
				"interactions/slash-commands",
				"interactions/message-components",
				"interactions/user-message-commands",
				"interactions/modals",
			],
		},
		{
			type: "category",
			label: "Популярные темы",
			link: { type: "doc", id: "popular-topics/intro" },
			items: [
				"popular-topics/threads",
				"popular-topics/embeds",
				"popular-topics/reactions",
				"popular-topics/webhooks",
				"popular-topics/permissions",
				"popular-topics/errors",
				"popular-topics/intents",
			],
		},
		{
			type: "category",
			label: "Часто задаваемые вопросы",
			link: { type: "doc", id: "faq/intro" },
			items: [
				"faq/general",
				"faq/administrative",
				"faq/coroutines",
				"faq/extensions",
				"faq/good-practices",
			],
		},
	],
};

module.exports = sidebars;
