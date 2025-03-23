/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Bind resources to your worker in `wrangler.jsonc`. After adding bindings, a type definition for the
 * `Env` object can be regenerated with `npm run cf-typegen`.
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

export default {
	async fetch(request, env, ctx): Promise<Response> {
		const { method, url, headers } = request;
		const body = await request.text();

		const urlObj = new URL(url);
		const json = urlObj.searchParams.get("json");

		if (json === "true") {
			const data = { 
				method,
				protocol: request.cf?.httpProtocol,
				path: urlObj.pathname,
				path_with_query: urlObj.href.replace(urlObj.origin, ""),
				query: Object.fromEntries(urlObj.searchParams),
				body,
				headers: Object.fromEntries(headers),
				cf: request.cf
			}
			return new Response(JSON.stringify(data), {
				status: 200,
				headers: {
					"Content-Type": "application/json",
				},
			});
		} else {
			return new Response((
				`${method} ${urlObj.href.replace(urlObj.origin, "")} ${request.cf?.httpProtocol}\n\n` + //  ${request.cf?.tlsVersion}
				Object.entries(Object.fromEntries(headers)).map(([k, v]) => `${k}: ${v}`).join("\n") +
				(body ? `\n\n${body}` : "")
			), {
				status: 200,
				headers: {
					"Content-Type": "application/json",
				},
			});
		}

		console.log
		(
			`Request: ${method} ${url}\n` +
			`Headers: ${JSON.stringify(Object.fromEntries(headers))}\n` +
			`Body: ${body}`
		);
	},
} satisfies ExportedHandler<Env>;
