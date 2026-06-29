from src.agents.agents import build_reader_agent, critic_chain, web_search_agent, writer_chain

def run_research_pipeline(topic : str)->dict:

    state = {}
    print('step - 1 search agent is working')
    search_agent = web_search_agent()
    search_result = search_agent.invoke({
        'messages':[('user',f'Find recent reliable detailed information about: {topic}')]
    })

    state['search_result'] = search_result['messages'][-1].content

    print(state['search_result'])

    print('Step - 2 Reader Agent is scrapping tip resources')

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({'messages':[('user',
                                                     f'Based on the following search results about {topic} \
                                                     pick the most relevant URL and scrape ot for deeper content.\
                                                     Search results : {state['search_result']}')]})
    
    state['scraped_content'] = reader_result['messages'][-1].content

    print('Writer is Drafting the report')

    research_combined = (f'Search Results : {state["search_result"]}',f'Detailed Scraped Content:{state['scraped_content']}')

    state['report'] = writer_chain.invoke({
        'topic': topic,
        'research': research_combined
    })

    print(f'Final Report :{state["report"]}')

    print('Crtique is reviewing the report')

    state['feedback'] = critic_chain.invoke({'report':state['report']})

    print(f'Final Report :{state["feedback"]}')

    print(state)

    return state


    
