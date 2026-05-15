export const meta = {
	name: 'Kridtin Chawalratikool',
	email: 'kridtin.ch@gmail.com',
	phone: '083-038-2618',
	github: 'https://github.com/KridtinC',
	linkedin: 'https://www.linkedin.com/in/kridtinc',
	role: 'Senior Software Engineer',
	company: 'LINE MAN Wongnai',
	bio: 'A Software Engineer with 6 years of experience, specializing in the architectural design and development of end-to-end applications. Primary languages are Go and TypeScript — always eager to explore new tools and techniques.',
	about: [
		"I'm a Software Engineer based in Bangkok, Thailand, with a passion for building robust, scalable systems. I specialize in architecting end-to-end applications and thrive at the intersection of backend performance and frontend polish.",
		"Currently at LINE MAN Wongnai as a Senior Software Engineer, I've been a key contributor in launching a new LINE MAN product from the ground up — from team setup and culture-building to design, implementation, and deployment.",
		"Outside of work, I enjoy building side projects that scratch my own itch — from Pokédex web apps to data dashboards. I hold a B.Eng. in Computer Engineering from Chulalongkorn University (GPA 3.09)."
	]
};

export const experience = [
	{
		company: 'LINE MAN Wongnai',
		role: 'Senior Software Engineer',
		period: 'Oct 2024 – Present',
		location: 'Bangkok, TH · Hybrid',
		url: 'https://lmwn.com',
		note: 'Promoted to Senior · Feb 2026',
		bullets: [
			'Key contributor in launching the new LINE MAN product from the ground up',
			'Took initiative in team setup, culture-building, and defining workflows for a newly formed team',
			'Facilitated discussions, shared updates, and improved processes through EM/PM collaboration',
			'Drove effective cross-team communication with other service owners',
			'Translated product features into actionable tasks, ensuring clarity and alignment within the team',
			'Proactively worked with PM to assess feasibility, communicate technical constraints, and align on solutions',
			'Delivered high-quality, on-time implementations with strong ownership from design to deployment'
		]
	},
	{
		company: 'LINE Company (Thailand)',
		role: 'Solution Engineer',
		period: 'Jul 2022 – Aug 2024',
		location: 'Bangkok, TH · Hybrid',
		url: 'https://linecorp.com',
		bullets: [
			'Developed new features for Social Commerce Platform (LINE Shopping, MyShop) to enhance user experience and drive engagement',
			'Collaborated with cross-functional teams to implement effective solutions for requirements breakdown, ensuring seamless integration',
			'Conducted demonstrations with the business team to showcase new features, leading to successful product launches',
			'Provided timely support for incidents, investigating issues to ensure customer satisfaction'
		]
	},
	{
		company: 'KASIKORN Business-Technology Group',
		role: 'Software Engineer',
		period: 'Jul 2020 – Jun 2022',
		location: 'Nonthaburi, TH · Hybrid',
		url: 'https://kbtg.tech',
		bullets: [
			'Implemented Centralized Back Office financial application for KBank users with various features',
			'Designed databases and technical flows to meet business requirements with a focus on performance optimization',
			'Created Control-M specifications for system batch processes',
			'Developed and tested REST APIs for client web applications; utilized gRPC for server-side communication following SOLID and Clean Architecture principles',
			'Conducted code peer reviews to ensure accuracy of business logic and performed unit testing',
			'Improved the automated test pipeline to provide more readable and trackable logs for easier identification of failed tests',
			'Provided support to the test team and NFT team in identifying and resolving functional defects and performance issues',
			'Engaged in meetings with legacy application teams to propose appropriate solutions for each requirement',
			'Assisted the Technical Lead in deployment processes and incident resolution'
		]
	},
	{
		company: 'True Corporation',
		role: 'Full Stack Web Developer (Internship)',
		period: 'Jun 2019 – Aug 2019',
		location: 'Bangkok, TH',
		url: null,
		bullets: [
			'Collaborated with the team lead to design the architecture diagram and POC for a billing inquiry system using the MVC pattern',
			'Developed an online customer billing website to enable customers to inquire about their invoices and receipts',
			'Implemented APIs to gather data from the company\'s existing billing data stored in relational databases',
			'Developed APIs to generate invoices and receipts as PDF files using the Jasper Report file format'
		]
	}
];

export const volunteering = [
	{
		role: 'Solution Engineer (Volunteer)',
		org: 'LINE Company (Thailand)',
		period: 'May 2023 · 1 mo',
		category: 'Education',
		description: 'Served as a host for Go training sessions for the LINE Rookie (Intern) program.',
		link: 'https://www.canva.com/design/DAFju6V8LY8/kpYlWz36qAXrTW_WzUffsw/edit',
		linkLabel: 'View slides'
	},
	{
		role: 'Teaching Staff',
		org: 'Chulalongkorn University',
		period: 'May 2017 · 1 mo',
		category: 'Education',
		description: 'Taught Python programming to high school students.',
		link: null,
		linkLabel: null
	}
];

export const skills = {
	ai: [
		'Cursor AI', 'Model Context Protocol (MCP)', 'Context Engineering',
		'Architectural Design', 'SOLID Design Principles'
	],
	experienced: [
		'Go', 'TypeScript', 'Java', 'Python', 'SQL',
		'React', 'Next.js', 'Vue', 'Nuxt', 'AngularJS',
		'Node.js', 'Express.js',
		'MySQL', 'MongoDB', 'YottaDB', 'Redis',
		'GraphQL', 'gRPC', 'Kafka', 'RabbitMQ', 'Apache Airflow',
		'Docker', 'Git', 'GitHub Actions', 'Shell'
	],
	familiar: [
		'Elasticsearch', 'NGINX', 'BMC Control-M',
		'AWS', 'K8s', 'Kotlin', 'Android'
	]
};

export const projects = [
	{
		id: 'pocketdex',
		num: '01',
		name: 'Pocketdex',
		description:
			'Full-stack Pokédex covering all 1025 Pokémon. Built with Next.js 14, Go backend, and MongoDB. Features team builder, type matchup calculator, and regional dex filters.',
		stack: ['Next.js 14', 'Go', 'MongoDB', 'TypeScript'],
		url: 'https://github.com/KridtinC/pocketbase',
		hasDemo: true,
		demoType: 'iframe',
		demoUrl: 'https://pocketbase.pages.dev/'
	},
	{
		id: 'covid19-dashboard',
		num: '02',
		name: 'COVID-19 Dashboard',
		description:
			'Interactive data visualization dashboard built with Python and Plotly Dash, tracking global COVID-19 statistics sourced from CSSEGIS data.',
		stack: ['Python', 'Plotly Dash', 'Pandas'],
		url: 'https://github.com/KridtinC/covid19-dashboard',
		hasDemo: true,
		demoType: 'iframe',
		demoUrl: 'https://covid19-dashboard-opzk.onrender.com/'
	}
];
