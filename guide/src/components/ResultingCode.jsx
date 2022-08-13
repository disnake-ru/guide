import React from "react";
import {useLocation} from "@docusaurus/router";

export default function ResultingCode() {
	const location = useLocation();
	const codeSampleURL = 'https://github.com/disnake-ru/guide/tree/main/code-samples/';

	return(
		<>
			<p>
			Код, представленный на этой странице, можно найти в нашем репозитории GitHub{' '}
				<a href={codeSampleURL + location.pathname.slice(1)} target="_blank" rel="noopener noreferrer">здесь</a>.
			</p>
		</>
	);
};
