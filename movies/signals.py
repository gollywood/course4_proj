from movies.tasks import notify_of_new_search_term

notify_of_new_search_term.delay(instance.term)