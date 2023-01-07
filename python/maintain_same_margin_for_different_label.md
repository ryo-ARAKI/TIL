# 異なる軸ラベルに対して同一のプロット領域を確保したい

- マージンを自動調整する

  ```python
  plt.tight_layout()  # フォントサイズの影響を吸収する
  plt.savefig(
      filename + '.png',
      dpi=300,
      bbox_inches='tight', pad_inches=0.1  # 余白の設定
  )
  ```

  - この場合，軸ラベルの高さが異なると保存された画像でプロット領域の大きさが異なってしまう
- マージンを `subplots_adjust` でマニュアル制御する

  ```python
  plt.tight_layout()
  plt.subplots_adjust(left=0.2, right=0.95, top=0.95, bottom=0.25)
  plt.savefig(
      filename + '.png',
      dpi=300
  )
  ```

  - 異なる軸ラベルが収まるようなマージンを設定すれば，保存された画像でまったく同じプロット領域が得られる．
