import recorder
import transcript
import renderer
import solver
import steps_converter
import llm_bridge


if __name__ == "__main__":
    record = recorder.start_record()
    formula = transcript.audio_to_latex(record)
    renderer.render(formula)
    result = solver.evaluate(formula)
    prompt_solve = llm_bridge.build_prompt_solve(formula, result)
    print(prompt_solve)
    res = llm_bridge.get_response("gpt-4", prompt_solve)
    print(res)
    steps = steps_converter.convert(res)
    steps_converter.render_steps(steps)