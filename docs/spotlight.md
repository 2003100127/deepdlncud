# Spotlight

## Sun's series work in drug discovery

Jianfeng Sun spearheaded a research plan dedicated to the AI-based discovery of small molecule therapeutics targeting non-coding RNAs and proteins, working in collaboration with both experimentalists and computational scientists across the globe. He has released 5 studies as in [Table 1](#tbl:jsun-sysbiol-work). The development of DeepdlncUD was one of the series studies of this project.

:::{table} Sun's work in drug discovery. ➵ stands for the current work.
:label: tbl:jsun-sysbiol-work
:align: center

<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr style="background-color:#d9d9d9;">
      <th>Field</th>
      <th>Molecule</th>
      <th>Tool name</th>
      <th>Function</th>
      <th>Technology</th>
      <th>Publication</th>
    </tr>
  </thead>
  <tbody>
    <!-- Systems Biology -->
    <tr>
      <td rowspan="3"><strong>Systems Biology</strong></td>
      <td rowspan="2">noncoding RNA</td>
      <td><strong>DeepsmirUD</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.3390/ijms24031878" title="DeepsmirUD">Sun et al., 2023</a>.
        <em>International Journal of Molecular Sciences</em>
      </td>
    </tr>
    <tr>
      <td style="background: -webkit-linear-gradient(20deg, #09009f, #E743D9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"><strong>➵DeepdlncUD</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.compbiomed.2023.107226" title="DeepdlncUD">Sun et al., 2023</a>.
        <em>Computers in Biology and Medicine</em>
      </td>
    </tr>
    <tr>
      <td>protein</td>
      <td><strong>Drutai</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.ejmech.2023.115500" title="Drutai">Sun et al., 2023</a>.
        <em>European Journal of Medicinal Chemistry</em>
      </td>
    </tr>
    <!-- Structural Biology -->
    <tr>
      <td rowspan="2"><strong>Structural Biology</strong></td>
      <td rowspan="2">protein</td>
      <td><strong>DeepHelicon</strong></td>
      <td><em>structural prediction</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.jsb.2020.107574" title="DeepHelicon">Sun and Frishman, 2020</a>.
        <em>Journal of Structural Biology</em>
      </td>
    </tr>
    <tr>
      <td><strong>DeepTMInter</strong></td>
      <td><em>protein-protein interaction prediction</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.csbj.2021.03.005" title="DeepTMInter">Sun and Frishman, 2021</a>.
        <em>Computational and Structural Biotechnology Journal</em>
      </td>
    </tr>
  </tbody>
</table>
:::

## Feature of the computational method

Our approach centers on a computation-led framework that reconstructs small molecule–ncRNA relationships as an alternative to traditional count matrix-based differential expression (DE) analyses. Instead of relying on DE results, we predict the upregulation or downregulation of ncRNA expression mediated by small molecules. For each small molecule, genes are first categorized into upregulated or downregulated groups, and then ranked within each group based on the predicted likelihood of expression change. Building on [our initial instance](https://doi.org/10.3390/ijms24031878) in applying this framework to identify candidate drugs targeting miRNAs , we extended its applicability by integrating DeepdlncUD, a tool specifically designed for lncRNA targets. The drug-like molecules inferred through this approach hold promise for [both drug repositioning and the discovery of novel therapeutics](https://doi.org/10.1093/bib/bbab161). To the best of our knowledge, this represents the first fully automated, computation-driven drug inference pipeline based on connectivity scores that relies solely on molecular sequences to accomplish an end-to-end discovery process. 

:::{seealso}
The DeepdlncUD tool introduced in this work is instrumental in addressing a critical gap in lncRNA-targeted drug discovery, particularly given that [this class of ncRNAs is estimated to regulate approximately 30% of human genes](https://doi.org/10.1016/j.molmed.2018.01.001).
:::

## Support for running multiple cases

In this updated version `0.0.1` in PyPI, we tuned **DeepdlncUD** to make it available to run multiple instances of predicting SM-lncRNA regulation types. This should be seen as a major update because it is very important for researchers to screen large-scale regulation types with reduced oprations from their back ends.

## Runtime

**DeepdlncUD** was developed based on molecular sequences alone. It runs in a very fast speed than those supported with complex data structures and settings, making it an ideal tool for biochemical researchers.

:::{caution} Comparison
The previous version of **DeepdlncUD** runs on one regulation type prediction each time, and thus deep learning libraries will be mounted each time for multiple instances, making it time-consuming.
:::